# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

import json
from pathlib import Path

from app.baseline.contracts import BBox, Control, InterfaceAsset, Observation


def generate_draft(observation: Observation) -> InterfaceAsset:
    return InterfaceAsset(
        asset_id=f"{observation.screen_id}-baseline-v1",
        screen_id=observation.screen_id,
        responsibility=f"Describe and operate the synthetic {observation.screen_id} screen",
        controls=list(observation.controls),
        reviewed=False,
        artifact_is_authorization=False,
    )


def save_asset(asset: InterfaceAsset, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asset.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")


def load_asset(path: Path) -> InterfaceAsset:
    data = json.loads(path.read_text(encoding="utf-8"))
    controls = [Control(**{**item, "bbox": BBox(**item["bbox"])}) for item in data["controls"]]
    return InterfaceAsset(
        asset_id=data["asset_id"],
        screen_id=data["screen_id"],
        responsibility=data["responsibility"],
        controls=controls,
        reviewed=bool(data.get("reviewed")),
        artifact_is_authorization=False,
    )


def approve_draft(draft_path: Path, reviewed_path: Path) -> InterfaceAsset:
    asset = load_asset(draft_path)
    asset.reviewed = True
    save_asset(asset, reviewed_path)
    return asset
