# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

from dataclasses import dataclass

from app.baseline.contracts import Control, Observation


@dataclass(frozen=True)
class LocatedCandidate:
    control: Control
    click_point: tuple[int, int]
    score: float
    capture_id: str
    viewport_size: tuple[int, int]
    source: str = "deterministic_semantic_baseline"


def locate(observation: Observation, semantic_target: str) -> LocatedCandidate:
    target = semantic_target.casefold().strip()
    ranked = sorted(
        observation.controls,
        key=lambda control: (
            control.semantic_name.casefold() != target,
            target not in control.semantic_name.casefold(),
            control.control_id,
        ),
    )
    if not ranked or target not in ranked[0].semantic_name.casefold():
        raise LookupError(f"No current-screen candidate for: {semantic_target}")
    exact = ranked[0].semantic_name.casefold() == target
    return LocatedCandidate(ranked[0], ranked[0].bbox.center, 1.0 if exact else 0.8, observation.capture_id, observation.viewport_size)
