"""Opt-in real retrieval plus deterministic evidence-bound A2-3 smoke coverage."""

from __future__ import annotations

import json
import os
from collections.abc import Sequence
from dataclasses import dataclass

import pytest

from decision_agent.agents.answerability_reviewer import AnswerabilityDecision
from decision_agent.agents.evidence_selector import EvidenceSelection
from decision_agent.agents.grounded_answer import AnswerDraft
from decision_agent.retrieval.evidence_context import EvidenceItem
from decision_agent.retrieval.factory import build_enterprise_retrieval_pipeline
from decision_agent.workflows.knowledge_qa import (
    Answerability,
    build_knowledge_qa_graph,
    run_knowledge_qa,
)

pytestmark = pytest.mark.integration


@dataclass(frozen=True)
class EvidenceBoundCase:
    """Fixture facts used only when current selected Evidence explicitly contains them."""

    selection_fact: str
    required_fact: str
    answerability: str
    answer: str
    missing_information: str | None
    decision_reason: str


_CASES = (
    EvidenceBoundCase(
        selection_fact="Model A Original Battery",
        required_fact="Model A Original Battery",
        answerability="answerable",
        answer="The base warranty period for Product A's original battery is 12 months.",
        missing_information=None,
        decision_reason="The selected evidence explicitly states the base warranty period for Model A Original Battery.",
    ),
    EvidenceBoundCase(
        selection_fact="Procurement",
        required_fact="Procurement",
        answerability="answerable",
        answer="A standard procurement of 180,000 CNY falls in the range of 50,000 to 200,000 CNY, approved by the Procurement Director.",
        missing_information=None,
        decision_reason="The selected evidence explicitly defines the approval authority for this amount range.",
    ),
    EvidenceBoundCase(
        selection_fact="Information Security",
        required_fact="Information Security",
        answerability="answerable",
        answer="Access to L3 confidential data requires joint approval from the Department Head and the Information Security Office.",
        missing_information=None,
        decision_reason="The selected evidence explicitly specifies both required approvals for L3 data access.",
    ),
    EvidenceBoundCase(
        selection_fact="Repair",
        required_fact="free repair warranty duration",
        answerability="unanswerable",
        answer="",
        missing_information="Additional free warranty duration after repair completion",
        decision_reason="The selected evidence only specifies repair procedures and does not specify additional warranty days after repair.",
    ),
)


class EvidenceBoundSelector:
    """Select only fixture facts that are present in this request's actual Evidence."""

    def __init__(self) -> None:
        self.case: EvidenceBoundCase | None = None

    async def select(
        self,
        *,
        user_query: str,
        evidence_context: str,
        retrieval_evidence: Sequence[EvidenceItem],
    ) -> EvidenceSelection:
        del user_query, evidence_context
        assert self.case is not None
        selected = [item for item in retrieval_evidence if self.case.selection_fact in item.content]
        return EvidenceSelection(
            selected_evidence_ids=[f"[{item.evidence_id}]" for item in selected],
            selection_reason="Selected fixture-direct Evidence."
            if selected
            else "No fixture-direct Evidence matched.",
        )


class EvidenceBoundReviewer:
    """Decide only from the fact visible in the selected Evidence subset."""

    def __init__(self) -> None:
        self.case: EvidenceBoundCase | None = None

    async def review(
        self,
        *,
        user_query: str,
        selected_evidence_context: str,
        selected_evidence: Sequence[EvidenceItem],
    ) -> AnswerabilityDecision:
        del user_query, selected_evidence_context
        assert self.case is not None
        required_fact_is_present = any(
            self.case.required_fact in item.content for item in selected_evidence
        )
        if self.case.answerability == "answerable":
            assert required_fact_is_present
            return AnswerabilityDecision(
                answerability="answerable",
                missing_information=None,
                decision_reason=self.case.decision_reason,
            )
        assert not required_fact_is_present
        return AnswerabilityDecision(
            answerability="unanswerable",
            missing_information=self.case.missing_information,
            decision_reason=self.case.decision_reason,
        )


class EvidenceBoundGenerator:
    """Generate only from the selected direct fact, never from question text or labels."""

    def __init__(self) -> None:
        self.calls = 0
        self.case: EvidenceBoundCase | None = None

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
        del user_query, selected_evidence_context, missing_information, decision_reason
        assert answerability == "answerable"
        self.calls += 1
        assert self.case is not None and self.case.answerability == "answerable"
        matches = [item for item in selected_evidence if self.case.required_fact in item.content]
        if not matches:
            raise AssertionError("generator received no fixture-direct Evidence")
        citation = f"[{matches[0].evidence_id}]"
        return AnswerDraft(answer=f"{self.case.answer}{citation}", citations=[citation])


@pytest.mark.asyncio
async def test_real_retrieval_four_question_smoke() -> None:
    if os.getenv("RUN_KNOWLEDGE_QA_SMOKE") != "1":
        pytest.skip("set RUN_KNOWLEDGE_QA_SMOKE=1 to run cached real retrieval smoke")

    queries = (
        "How long is the base warranty period for Product A's original battery?",
        "Who needs to approve a standard procurement request of 180,000 CNY?",
        "What approvals are required to access L3 confidential data?",
        "How many days of free repair warranty does the company commit to after repairing Product A?",
    )
    generator = EvidenceBoundGenerator()
    selector = EvidenceBoundSelector()
    reviewer = EvidenceBoundReviewer()
    pipeline = build_enterprise_retrieval_pipeline("datasets/enterprise_kb/m2c1")
    try:
        await pipeline.initialize()
        graph = build_knowledge_qa_graph(
            retrieval_pipeline=pipeline,
            evidence_selector=selector,
            answerability_reviewer=reviewer,
            answer_generator=generator,
        )
        results = []
        for query, case in zip(queries, _CASES, strict=True):
            selector.case = reviewer.case = generator.case = case
            results.append(await run_knowledge_qa(graph, user_query=query))
    finally:
        await pipeline.close()

    audit_output = [
        {
            "query": query,
            "raw_evidence": [
                {"evidence_id": item.evidence_id, "document_id": item.document_id}
                for item in result.retrieval_evidence
            ],
            "selected_evidence": [
                {"evidence_id": item.evidence_id, "document_id": item.document_id}
                for item in result.selected_evidence
            ],
            "answerability": result.answerability,
            "missing_information": result.missing_information,
            "decision_reason": result.decision_reason,
            "answer": result.answer,
            "citations": result.citations,
            "generator_called": result.answerability is Answerability.ANSWERABLE,
        }
        for query, result in zip(queries, results, strict=True)
    ]
    print(json.dumps(audit_output, ensure_ascii=False))

    assert [result.answerability for result in results] == [
        Answerability.ANSWERABLE,
        Answerability.ANSWERABLE,
        Answerability.ANSWERABLE,
        Answerability.UNANSWERABLE,
    ]
    assert "12 months" in (results[0].answer or "")
    assert "Procurement Director" in (results[1].answer or "")
    assert "Department Head" in (results[2].answer or "")
    assert "Information Security Office" in (results[2].answer or "")
    q010 = results[3]
    assert q010.citations == []
    assert q010.answer is not None and not any(character.isdigit() for character in q010.answer)
    assert generator.calls == 3
