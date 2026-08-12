# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

from app.baseline.contracts import ActionPlan, InterfaceAsset


def decide(asset: InterfaceAsset, goal: str) -> ActionPlan:
    if not asset.reviewed:
        raise PermissionError("Agent may only consume a reviewed interface asset")
    goal_text = goal.casefold()
    for control in asset.controls:
        if "report" in goal_text and "report" in control.semantic_name.casefold():
            return ActionPlan("open-report", control.semantic_name, control.allowed_action, "report", [asset.asset_id])
    raise LookupError(f"Reviewed asset has no semantic action for goal: {goal}")
