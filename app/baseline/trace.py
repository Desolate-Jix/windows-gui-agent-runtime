# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class TraceRecorder:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def record(self, event_type: str, payload: dict[str, Any]) -> None:
        event = {"time": datetime.now(timezone.utc).isoformat(), "event_type": event_type, "payload": payload}
        with self.path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(event, ensure_ascii=False) + "\n")
