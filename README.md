# Windows GUI Agent Runtime

An early-stage, experimental baseline for learning a GUI interface, accepting human review, reusing the reviewed asset, and keeping every actual operation behind an independent Gate and Trace boundary.

Copyright © 2026 Wenqing Ji

## Problem

Screenshot-first GUI agents often repeat expensive interpretation and can blur the boundary between a learned hint and permission to act. This project keeps those concerns separate: Learn Mode produces a reusable asset; Agent chooses intent; Operation relocates on the current observation; Gate decides whether the action is allowed; Trace records evidence; verification checks the effect.

## Architecture

```text
Observe -> Agent -> Gate -> Operation -> Trace -> Observe/Verification
             ^
             |
generated draft -> human review -> reviewed interface asset
```

Workflow and interface assets are reusable knowledge, **not execution authorization**. The public v0.1 demo uses a deterministic synthetic adapter so it can be reproduced without accounts, private data, websites, model weights, or cloud services.

The copied `app.runtime_architecture`, `app.gate`, `modules.region`, and `modules.validation` packages expose public contracts and baseline utilities. The synthetic demo deliberately uses the smaller `app.baseline` composition root; the presence of a utility package does not imply that advanced private recognition is included or active.

## Key concepts

- **Agent**: converts a goal into a semantic action using a reviewed asset.
- **Operation**: owns current observation and the synthetic action adapter.
- **Gate**: rejects stale, ambiguous, low-confidence, or destructive actions.
- **Trace**: records the plan, candidate, decision, and post-action verification.
- **Learn/Review**: creates a draft that must be reviewed before Agent consumption.

## Installation

```powershell
git clone https://github.com/Desolate-Jix/windows-gui-agent-runtime.git
cd windows-gui-agent-runtime
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Quick start

Run the complete deterministic closure:

```powershell
python examples\local_demo.py
```

Expected result: a generated draft is saved, reviewed, reused by Agent, relocated against a fresh observation, allowed by Gate, executed by the synthetic adapter, traced, and verified on the resulting screen.

## Minimal review UI

```powershell
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`. Generate a draft, approve it, then run the gated action. For a manual JSON review flow, run `python examples\local_demo.py --prepare-only`, edit `.oss-demo-state/generated_draft.json`, then approve it through the local page.

## Safety model

- Unreviewed assets cannot be consumed by Agent.
- Learned assets never authorize execution.
- Relocation uses a fresh capture identifier and current viewport; Gate rejects candidates whose capture identifier does not match the current observation.
- The click point must remain inside the current candidate bounding box.
- Destructive action vocabulary such as submit, send, confirm, payment, and delete is blocked in the baseline.
- Every allowed action produces pre-action and post-action evidence.

## Project status and limitations

This is an experimental OSS baseline, not a production automation product. The bundled demo is synthetic and deterministic. It does not claim model accuracy, general GUI reliability, autonomous operation, live website compatibility, or production readiness. Advanced private recognition, reranking, model prompts, website adapters, and real-user assets are intentionally not included.

## Roadmap

- Add a replaceable screenshot/OCR/UIA observation adapter.
- Add a baseline Windows locator without weakening the Gate contract.
- Expand reviewed-asset editing and schema validation.
- Add reproducible fixtures and failure-oriented benchmarks.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security issues should follow [SECURITY.md](SECURITY.md).

## License

The project’s original public code is licensed under the GNU Affero General Public License v3.0 only (`AGPL-3.0-only`). See [LICENSE](LICENSE). Third-party dependencies retain their own licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
