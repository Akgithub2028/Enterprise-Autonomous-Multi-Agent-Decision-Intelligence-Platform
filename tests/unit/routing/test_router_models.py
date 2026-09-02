"""Unit contracts for bounded, non-executing routing decisions."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from decision_agent.routing.models import RequestRoute, RouterDecision


@pytest.mark.parametrize(
    ("route", "knowledge_subquery", "data_subquery"),
    [
        (RequestRoute.KNOWLEDGE, "Query procurement approval policy", None),
        (RequestRoute.DATA, None, "Query May sales revenue"),
        (RequestRoute.MIXED, "Query replenishment policy", "Query out-of-stock products"),
        (RequestRoute.UNSUPPORTED, None, None),
    ],
)
def test_router_decision_accepts_only_the_required_subquery_combination(
    route: RequestRoute,
    knowledge_subquery: str | None,
    data_subquery: str | None,
) -> None:
    decision = RouterDecision(
        route=route,
        normalized_query="Enterprise question",
        decision_reason="Routing rationale.",
        knowledge_subquery=knowledge_subquery,
        data_subquery=data_subquery,
        missing_information=None,
        confidence=0.8,
    )
    assert decision.route is route


@pytest.mark.parametrize(
    "overrides",
    [
        {"route": "unknown"},
        {"route": "knowledge", "knowledge_subquery": None},
        {"route": "knowledge", "data_subquery": "should_not_exist"},
        {"route": "data", "data_subquery": None, "knowledge_subquery": "should_not_exist"},
        {"route": "mixed", "data_subquery": None},
        {"route": "unsupported", "knowledge_subquery": "cannot_execute"},
        {"route": "unsupported", "sql": "DELETE FROM products"},
        {"confidence": -0.01},
        {"confidence": 1.01},
        {"decision_reason": "   "},
    ],
)
def test_router_decision_rejects_invalid_or_executable_contract_fields(
    overrides: dict[str, object],
) -> None:
    payload: dict[str, object] = {
        "route": "knowledge",
        "normalized_query": "What is the procurement approval process?",
        "decision_reason": "Question asks about policy.",
        "knowledge_subquery": "What is the company procurement approval process?",
        "data_subquery": None,
        "missing_information": None,
        "confidence": 0.8,
    }
    payload.update(overrides)
    with pytest.raises(ValidationError):
        RouterDecision.model_validate(payload)
