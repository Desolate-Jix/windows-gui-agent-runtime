# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal


@dataclass(frozen=True)
class BBox:
    x: int
    y: int
    width: int
    height: int

    def contains(self, point: tuple[int, int]) -> bool:
        px, py = point
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height

    @property
    def center(self) -> tuple[int, int]:
        return self.x + self.width // 2, self.y + self.height // 2


@dataclass(frozen=True)
class Control:
    control_id: str
    semantic_name: str
    role: str
    bbox: BBox
    allowed_action: Literal["click", "read"]
    observed_text: str = ""


@dataclass
class Observation:
    capture_id: str
    screen_id: str
    viewport_size: tuple[int, int]
    controls: list[Control]


@dataclass
class InterfaceAsset:
    asset_id: str
    screen_id: str
    responsibility: str
    controls: list[Control]
    reviewed: bool = False
    artifact_is_authorization: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ActionPlan:
    action_id: str
    semantic_target: str
    action_type: str
    expected_screen: str
    evidence_refs: list[str] = field(default_factory=list)


@dataclass
class GateResult:
    allowed: bool
    reason: str
    checks: list[str]
