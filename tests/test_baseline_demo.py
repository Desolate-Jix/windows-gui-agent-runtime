# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from pathlib import Path
import subprocess
import sys

import pytest

from app.baseline.pipeline import BaselineRuntime


def test_reviewed_asset_is_required(tmp_path: Path) -> None:
    runtime = BaselineRuntime(tmp_path)
    runtime.prepare()
    with pytest.raises(FileNotFoundError):
        runtime.run()


def test_demo_closes_learn_review_execute_loop(tmp_path: Path) -> None:
    runtime = BaselineRuntime(tmp_path)
    runtime.prepare()
    runtime.approve()
    result = runtime.run()
    assert result["verified"] is True
    assert result["before"] == "workspace"
    assert result["after"] == "report"
    assert result["gate"]["allowed"] is True
    assert (tmp_path / "trace.jsonl").read_text(encoding="utf-8").count("\n") == 4


def test_final_submit_is_blocked(tmp_path: Path) -> None:
    from app.baseline.contracts import ActionPlan
    from app.baseline.gate import evaluate
    from app.baseline.locator import locate

    runtime = BaselineRuntime(tmp_path)
    observation = runtime.ui.observe()
    candidate = locate(observation, "Final submit")
    result = evaluate(
        ActionPlan("submit", "Final submit", "click", "done"),
        candidate,
        current_capture_id=observation.capture_id,
    )
    assert result.allowed is False
    assert result.reason == "dangerous_action_blocked"
    assert result.checks == ["capture_id_present", "current_capture_bound", "point_inside_bbox"]


def test_stale_capture_is_rejected_before_point_or_action_checks(tmp_path: Path) -> None:
    from dataclasses import replace

    from app.baseline.contracts import ActionPlan
    from app.baseline.gate import evaluate
    from app.baseline.locator import locate

    runtime = BaselineRuntime(tmp_path)
    observation = runtime.ui.observe()
    candidate = replace(locate(observation, "Open incident report"), capture_id="capture-OLD")

    result = evaluate(
        ActionPlan("open", "Open incident report", "click", "report"),
        candidate,
        current_capture_id=observation.capture_id,
    )

    assert result.allowed is False
    assert result.reason == "stale_candidate_capture"
    assert result.checks == ["capture_id_present"]


def test_demo_runs_outside_repository_cwd(tmp_path: Path) -> None:
    repository_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(repository_root / "examples" / "local_demo.py"), "--workspace", str(tmp_path / "state")],
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert '"verified": true' in result.stdout


def test_public_packages_import() -> None:
    from app.main import app
    from app.runtime_architecture import RuntimeArchitectureSpec
    from modules.region import window_size_bucket
    from modules.validation import evaluate_counter_result

    assert app.title == "Windows GUI Agent Runtime OSS"
    assert RuntimeArchitectureSpec is not None
    assert window_size_bucket({"width": 640, "height": 420}) == "640x420"
    assert evaluate_counter_result(["1"], ["2"])["strict_success"] is True
