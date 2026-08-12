# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

from app.baseline.contracts import ActionPlan, GateResult
from app.baseline.locator import LocatedCandidate


DANGEROUS_TERMS = {"submit", "send", "confirm", "payment", "delete"}


def evaluate(plan: ActionPlan, candidate: LocatedCandidate, *, current_capture_id: str) -> GateResult:
    checks: list[str] = []
    if candidate.capture_id == "":
        return GateResult(False, "missing_capture_id", checks)
    checks.append("capture_id_present")
    if candidate.capture_id != current_capture_id:
        return GateResult(False, "stale_candidate_capture", checks)
    checks.append("current_capture_bound")
    if not candidate.control.bbox.contains(candidate.click_point):
        return GateResult(False, "point_outside_bbox", checks)
    checks.append("point_inside_bbox")
    combined = f"{plan.action_type} {plan.semantic_target}".casefold()
    if any(term in combined for term in DANGEROUS_TERMS):
        return GateResult(False, "dangerous_action_blocked", checks)
    checks.append("non_destructive_action")
    if candidate.score < 0.75:
        return GateResult(False, "candidate_confidence_too_low", checks)
    checks.append("candidate_confidence_sufficient")
    return GateResult(True, "low_risk_current_screen_candidate", checks)
