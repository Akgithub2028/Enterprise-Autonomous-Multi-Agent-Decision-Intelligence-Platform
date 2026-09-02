"""Opt-in A2-3 real Retrieval, Reviewer, and Generator smoke coverage."""

# ruff: noqa: RUF001

from __future__ import annotations

import json
import os
from collections.abc import Sequence

import pytest

from decision_agent.agents.answerability_reviewer import OpenAICompatibleAnswerabilityReviewer
from decision_agent.agents.evidence_selector import OpenAICompatibleEvidenceSelector
from decision_agent.agents.grounded_answer import AnswerDraft, OpenAICompatibleAnswerGenerator
from decision_agent.config import Settings
from decision_agent.retrieval.evidence_context import EvidenceItem
from decision_agent.retrieval.factory import build_enterprise_retrieval_pipeline
from decision_agent.workflows.knowledge_qa import (
    Answerability,
    KnowledgeQAState,
    build_knowledge_qa_graph,
    run_knowledge_qa,
)

pytestmark = pytest.mark.integration

_QUERIES = (
    "How long is the base warranty period for Product A's original battery?",
    "Who needs to approve a standard procurement request of 180,000 CNY?",
    "What approvals are required to access L3 confidential data?",
    "How many days of free repair warranty does the company commit to after repairing Product A?",
)


class CountingGenerator:
    """Record calls without exposing a provider response or configuration."""

    def __init__(self, delegate: OpenAICompatibleAnswerGenerator) -> None:
        self._delegate = delegate
        self.calls = 0

    async def generate(
        self,
        *,
        user_query: str,
        selected_evidence_context: str,
        selected_evidence: Sequence[EvidenceItem],
        answerability: str,
        missing_information: str | None,
        decision_reason: str,
    ) -> AnswerDraft:
        self.calls += 1
        return await self._delegate.generate(
            user_query=user_query,
            selected_evidence_context=selected_evidence_context,
            selected_evidence=selected_evidence,
            answerability=answerability,
            missing_information=missing_information,
            decision_reason=decision_reason,
        )


def _safe_audit(state: KnowledgeQAState, *, generator_called: bool) -> dict[str, object]:
    return {
        "raw_evidence": [
            {"evidence_id": item.evidence_id, "document_id": item.document_id}
            for item in state.retrieval_evidence
        ],
        "selected_evidence": [
            {"evidence_id": item.evidence_id, "document_id": item.document_id}
            for item in state.selected_evidence
        ],
        "answerability": state.answerability,
        "decision_reason": state.decision_reason,
        "missing_information": state.missing_information,
        "answer": state.answer,
        "citations": state.citations,
        "generator_called": generator_called,
        "error_codes": [
            {"code": error.code, "subcode": error.details.get("subcode")} for error in state.errors
        ],
    }


@pytest.mark.asyncio
async def test_real_llm_four_question_smoke() -> None:
    if os.getenv("RUN_KNOWLEDGE_QA_REAL_LLM_SMOKE") != "1":
        pytest.skip("set RUN_KNOWLEDGE_QA_REAL_LLM_SMOKE=1 to run A2-3 Level 3 smoke")

    settings = Settings()
    pipeline = build_enterprise_retrieval_pipeline("datasets/enterprise_kb/m2c1")
    generator = CountingGenerator(OpenAICompatibleAnswerGenerator.from_settings(settings))
    try:
        await pipeline.initialize()
        graph = build_knowledge_qa_graph(
            retrieval_pipeline=pipeline,
            evidence_selector=OpenAICompatibleEvidenceSelector.from_settings(settings),
            answerability_reviewer=OpenAICompatibleAnswerabilityReviewer.from_settings(settings),
            answer_generator=generator,
        )
        results_with_generator_calls = []
        for query in _QUERIES:
            calls_before = generator.calls
            result = await run_knowledge_qa(graph, user_query=query)
            results_with_generator_calls.append((result, generator.calls > calls_before))
    finally:
        await pipeline.close()

    results = [result for result, _ in results_with_generator_calls]
    audits = [
        _safe_audit(result, generator_called=generator_called)
        for result, generator_called in results_with_generator_calls
    ]
    print(json.dumps(audits, ensure_ascii=False))

    battery, procurement, l3, q010 = results
    assert battery.answerability is Answerability.ANSWERABLE
    assert any(term in (battery.answer or "").lower() for term in ("12 month", "twelve month", "12", "twelve"))
    assert battery.citations
    assert procurement.answerability is Answerability.ANSWERABLE
    assert any(term in (procurement.answer or "").lower() for term in ("procurement director", "procurement")) and procurement.citations
    assert l3.answerability is Answerability.ANSWERABLE
    assert any(term in (l3.answer or "").lower() for term in ("department head", "department"))
    assert l3.citations
    assert q010.answerability is Answerability.UNANSWERABLE
    assert q010.citations == []
    assert bool(q010.decision_reason)
    assert bool(q010.missing_information)
    assert q010.answer is not None and not any(character.isdigit() for character in q010.answer)
    assert generator.calls == 3
