"""High-level tool wrappers reuse existing Agent entry points without direct data access."""

from __future__ import annotations

import pytest

from decision_agent.tool_calling.tools import DataAgentTool, KnowledgeAgentTool
from decision_agent.workflows.data_agent import DataAgentState, DataAgentStatus
from decision_agent.workflows.knowledge_qa import Answerability, KnowledgeQAState


@pytest.mark.asyncio
async def test_knowledge_tool_projects_existing_knowledge_state(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = KnowledgeQAState(
        user_query="query",
        answerability=Answerability.ANSWERABLE,
        answer="Knowledge answer. [E1]",
        citations=["[E1]"],
        decision_reason="Evidence supported.",
    )

    async def fake_run(graph: object, *, user_query: str) -> KnowledgeQAState:
        assert graph == "graph"
        assert user_query == "subquery"
        return state

    monkeypatch.setattr("decision_agent.tool_calling.tools.run_knowledge_qa", fake_run)
    result = await KnowledgeAgentTool(graph="graph").run(query="subquery")
    assert result.model_dump() == {
        "status": "succeeded",
        "answer": "Knowledge answer. [E1]",
        "citations": ["[E1]"],
        "error_code": None,
    }


@pytest.mark.asyncio
async def test_data_tool_delegates_to_existing_mcp_backed_data_agent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = DataAgentState(
        query="query",
        status=DataAgentStatus.ANSWERABLE_FINAL,
        plan_status="ready",
        intent="query",
        planned_sql="SELECT product_id FROM products",
        decision_reason="Complete conditions.",
        data_evidence=(
            {
                "evidence_id": "D1",
                "normalized_sql": "SELECT product_id FROM products",
                "columns": ["product_id"],
                "rows": [["P100"]],
                "row_count": 1,
                "truncated": False,
                "accessed_tables": ["products"],
                "elapsed_ms": 1.0,
            },
        ),
        answer="Data answer. [D1]",
        citations=["[D1]"],
    )
    captured: dict[str, object] = {}

    async def fake_run_data_agent(**kwargs: object) -> DataAgentState:
        captured.update(kwargs)
        return state

    monkeypatch.setattr("decision_agent.tool_calling.tools.run_data_agent", fake_run_data_agent)
    factory = lambda: object()  # noqa: E731
    tool = DataAgentTool(
        planner=object(),  # type: ignore[arg-type]
        enterprise_data_client_factory=factory,  # type: ignore[arg-type]
        answer_generator=object(),  # type: ignore[arg-type]
    )
    result = await tool.run(query="subquery")
    assert captured["query"] == "subquery"
    assert captured["enterprise_data_client_factory"] is factory
    assert result.status == "succeeded"
    assert result.citations == ["[D1]"]
