# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

from app.baseline.contracts import BBox, Control, Observation


class SyntheticUI:
    """确定性本地 UI adapter；不依赖浏览器、网络或私人运行时。"""

    def __init__(self) -> None:
        self.screen_id = "workspace"
        self._counter = 0

    def observe(self) -> Observation:
        self._counter += 1
        controls = {
            "workspace": [
                Control("open_report", "Open incident report", "button", BBox(40, 60, 220, 48), "click", "Open report"),
                Control("final_submit", "Final submit", "button", BBox(40, 140, 220, 48), "click", "Submit"),
            ],
            "report": [
                Control("report_body", "Incident report content", "document", BBox(30, 40, 500, 260), "read", "Synthetic incident report"),
                Control("back_workspace", "Return to workspace", "button", BBox(30, 330, 190, 48), "click", "Back"),
            ],
        }[self.screen_id]
        return Observation(
            capture_id=f"capture-{self._counter}",
            screen_id=self.screen_id,
            viewport_size=(640, 420),
            controls=controls,
        )

    def click(self, control_id: str) -> None:
        transitions = {
            ("workspace", "open_report"): "report",
            ("report", "back_workspace"): "workspace",
        }
        key = (self.screen_id, control_id)
        if key not in transitions:
            raise ValueError(f"Synthetic operation is not supported: {key}")
        self.screen_id = transitions[key]
