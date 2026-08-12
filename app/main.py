# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Wenqing Ji

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from app.baseline.pipeline import BaselineRuntime


app = FastAPI(title="Windows GUI Agent Runtime OSS", version="0.1.0")
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
runtime = BaselineRuntime(REPOSITORY_ROOT / ".oss-demo-state")


@app.get("/", response_class=HTMLResponse)
def review_page() -> str:
    return """<!doctype html><meta charset='utf-8'><title>OSS Learn/Review Demo</title>
<style>body{font:16px system-ui;max-width:800px;margin:40px auto}button{margin:6px;padding:10px 16px}pre{background:#f4f6f8;padding:16px;white-space:pre-wrap}</style>
<h1>Learn / Review baseline</h1><p>This synthetic demo never controls a real application.</p>
<button onclick=call('/demo/prepare')>Generate draft</button><button onclick=call('/demo/approve')>Approve</button><button onclick=call('/demo/run')>Run gated action</button><pre id=o>Ready.</pre>
<script>async function call(u){let r=await fetch(u,{method:'POST'});o.textContent=JSON.stringify(await r.json(),null,2)}</script>"""


@app.post("/demo/prepare")
def prepare() -> dict[str, object]:
    return runtime.prepare()


@app.post("/demo/approve")
def approve() -> dict[str, object]:
    try:
        return runtime.approve()
    except FileNotFoundError as exc:
        raise HTTPException(409, "Generate a draft before approval") from exc


@app.post("/demo/run")
def run_demo() -> dict[str, object]:
    try:
        return runtime.run()
    except (FileNotFoundError, PermissionError, LookupError) as exc:
        raise HTTPException(409, str(exc)) from exc
