"""Opt-in real native-tool-calling smoke with deterministic safe high-level tool results."""

from __future__ import annotations

import os

import pytest

from decision_agent.config import Settings
from decision_agent.routing.models import RouterDecision
from decision_agent.tool_calling.models import AgentToolResult, NativeToolCallingStatus
from decision_agent.tool_calling.runtime import (
    OpenAICompatibleNativeToolCallingModel,
    run_native_tool_calling,
)

pytestmark = pytest.mark.integration


class DeterministicTool:
    def __init__(self, result: AgentToolResult) -> None:
        self.result = result
        self.calls: list[str] = []

    async def run(self, *, query: str) -> AgentToolResult:
        self.calls.append(query)
        return self.result


def _decision(route: str) -> RouterDecision:
    return RouterDecision(
        route=route,
        normalized_query="Enterprise question",
        decision_reason="Routing completed.",
        knowledge_subquery="What is the after-sales warranty policy for Product A?" if route == "knowledge" else None,
        data_subquery="Which product had the highest sales revenue in May?" if route == "data" else None,
        missing_information=None,
        confidence=0.9,
    )


@pytest.mark.asyncio
async def test_real_provider_uses_native_tool_calls_for_knowledge_and_data() -> None:
    """Use real tools/tool_calls only; fake tools avoid retrieval, MCP, and database execution."""
    if os.getenv("RUN_NATIVE_TOOL_CALLING_REAL_LLM_SMOKE") != "1":
        pytest.skip(
            "set RUN_NATIVE_TOOL_CALLING_REAL_LLM_SMOKE=1 to run the real native-tools smoke"
        )
    settings = Settings()
    if (
        settings.llm_api_key is None
        or settings.llm_base_url is None
        or settings.llm_model_name is None
    ):
        pytest.skip("LLM settings are not fully configured")
    model = OpenAICompatibleNativeToolCallingModel.from_settings(settings)
    knowledge = DeterministicTool(
        AgentToolResult(
            status="succeeded",
            answer="The warranty period for Product A's original battery is 12 months.[E1]",
            citations=["[E1]"],
        )
    )
    data = DeterministicTool(
        AgentToolResult(
            status="succeeded",
            answer="The product with the highest sales revenue in May is Aster Industrial Pump.[D1]",
            citations=["[D1]"],
        )
    )

    observed: list[dict[str, object]] = []
    for query, route in (
        ("What is the after-sales warranty policy for Product A?", "knowledge"),
        ("Which product had the highest sales revenue in May?", "data"),
    ):
        result = await run_native_tool_calling(
            user_query=query,
            decision=_decision(route),
            model=model,
            knowledge_tool=knowledge,
            data_tool=data,
        )
        assert result.status is NativeToolCallingStatus.COMPLETED
        assert result.tool_call_id is not None
        assert result.selected_tool == f"run_{route}_agent"
        observed.append(
            {
                "route": route,
                "selected_tool": result.selected_tool,
                "native_tool_call_id_present": True,
            }
        )
    assert knowledge.calls == ["What is the after-sales warranty policy for Product A?"]
    assert data.calls == ["Which product had the highest sales revenue in May?"]
    print({"native_tool_calling_smoke": observed})
