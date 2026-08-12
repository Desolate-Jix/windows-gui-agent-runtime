# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from app.baseline.agent import decide
from app.baseline.gate import evaluate
from app.baseline.learn import approve_draft, generate_draft, load_asset, save_asset
from app.baseline.locator import locate
from app.baseline.synthetic_ui import SyntheticUI
from app.baseline.trace import TraceRecorder


class BaselineRuntime:
    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace
        self.ui = SyntheticUI()
        self.trace = TraceRecorder(workspace / "trace.jsonl")
        self.draft_path = workspace / "generated_draft.json"
        self.reviewed_path = workspace / "reviewed_asset.json"

    def prepare(self) -> dict[str, object]:
        observation = self.ui.observe()
        draft = generate_draft(observation)
        save_asset(draft, self.draft_path)
        self.trace.record("generated_draft", {"capture_id": observation.capture_id, "asset_id": draft.asset_id})
        return draft.to_dict()

    def approve(self) -> dict[str, object]:
        asset = approve_draft(self.draft_path, self.reviewed_path)
        self.trace.record("human_review", {"asset_id": asset.asset_id, "reviewed": True})
        return asset.to_dict()

    def run(self, goal: str = "Open the incident report") -> dict[str, object]:
        asset = load_asset(self.reviewed_path)
        before = self.ui.observe()
        plan = decide(asset, goal)
        candidate = locate(before, plan.semantic_target)
        gate = evaluate(plan, candidate, current_capture_id=before.capture_id)
        self.trace.record("pre_click_decision", {"plan": asdict(plan), "candidate": asdict(candidate), "gate": asdict(gate)})
        if not gate.allowed:
            raise PermissionError(gate.reason)
        self.ui.click(candidate.control.control_id)
        after = self.ui.observe()
        verified = after.screen_id == plan.expected_screen
        self.trace.record("post_action_verification", {"before": before.screen_id, "after": after.screen_id, "verified": verified})
        return {"goal": goal, "decision": asdict(plan), "gate": asdict(gate), "before": before.screen_id, "after": after.screen_id, "verified": verified}
