# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

"""Region-click geometry helpers."""

from .geometry import (
    generate_zone_points,
    locate_mouse_tester_panel,
    normalized_point,
    window_rect,
    window_size_bucket,
)

__all__ = [
    "generate_zone_points",
    "locate_mouse_tester_panel",
    "normalized_point",
    "window_rect",
    "window_size_bucket",
]
