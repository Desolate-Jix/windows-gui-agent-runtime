# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from app.baseline.pipeline import BaselineRuntime


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the deterministic OSS baseline demo")
    parser.add_argument("--workspace", type=Path, default=REPOSITORY_ROOT / ".oss-demo-state")
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    runtime = BaselineRuntime(args.workspace)
    draft = runtime.prepare()
    print(json.dumps({"generated_draft": draft}, indent=2))
    if args.prepare_only:
        print(f"Edit {runtime.draft_path}, then approve through the API or Python helper.")
        return
    runtime.approve()
    print(json.dumps(runtime.run(), indent=2))


if __name__ == "__main__":
    main()
