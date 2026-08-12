# Source Provenance

This file records the origin of the OSS v0.1 release candidate without including the private repository history or location. The private repository remains separate and is not required at runtime.

## Allowlisted source files

The following files were copied from an allowlisted private source snapshot, then received the OSS SPDX/copyright header. `app/runtime_architecture/contracts.py` additionally replaces one domain-specific responsibility phrase with a generic equivalent; no runtime behavior is changed by that wording update.

| Public path | Source-relative path | Source SHA-256 | Public SHA-256 |
|---|---|---|---|
| `app/gate/actions.py` | `app/gate/actions.py` | `3b9bd9235a94cc3b23029b3e93bc1893a7380148a631b60ebc512c9c04f542b4` | `daa3499f310d33b22b1cbb1196546881c1f9b0233c36d7939ffb3f5c28fa2f15` |
| `app/gate/danger.py` | `app/gate/danger.py` | `c70a19bec275edf0f147251a66f7826bc7b22e38f84b84667f468c0e0f7b7f42` | `a0e41fbef84c9be3d84a5de718102996c69516f318a3f18088317c290d68cd04` |
| `app/runtime_architecture/__init__.py` | `app/runtime_architecture/__init__.py` | `790f71288f9c1dabede6113260abcfb70ffef6e21f04a29b94831b6697f452f8` | `1830505e6309c80148dc45138d1beb1a3e8325d206ed708ec5cafe4c12cc9334` |
| `app/runtime_architecture/contracts.py` | `app/runtime_architecture/contracts.py` | `9bbfa1e87dd8699da7db99d89402f46ca187b1b85df648bde7f59daa7394f428` | `cf973bc9a84ed5c6f704632e1718ca7267e5ddf50da0f0f9e0c0fe01c07a490d` |
| `app/runtime_architecture/profiles.py` | `app/runtime_architecture/profiles.py` | `ec0e694321624373ca7eac3369f4cfa28cf0d279fde3e40438a2807b933645ac` | `2b250d092a4132e8dcd0a014df1c81f8d7b8119cce384f69111fcc82fba6c4b9` |
| `modules/region/__init__.py` | `modules/region/__init__.py` | `8e966e8a1f0a74fa50297a2349c12d65b9dea883aba9de8edaaeb3dfea576914` | `9333d57683f83c821ad727f0258e821070a2c03a64a87d7b2c3e014bb1e65cd9` |
| `modules/region/geometry.py` | `modules/region/geometry.py` | `ce41bf6ba39295dd58685a60c7f76e73567e1fac9f182346b2ef5cb39653afa4` | `ee090e0d630e4fdd726457dd76058a81447214b3d0d8aa25dad649635db6ba9f` |
| `modules/validation/__init__.py` | `modules/validation/__init__.py` | `30458cc778d4400b38782d4579b0a196a94653b1523e4339632cdb79355d77c8` | `a466495c005c239f4246b3349bbbc5b6684273c68bc91074fd5f80491cf8c5ff` |
| `modules/validation/counter.py` | `modules/validation/counter.py` | `d3da75f2a6d4fa45cf07df1c274d5250d930fa73dd7e3481f473043d8154a8cf` | `fc35b6415332d07dbbbc2098e4a309be577edd64b990e5a5d37585649737dafe` |

## New OSS-original implementation

All other Python implementation, tests, examples, and public documentation in this repository were written specifically for this OSS baseline and are not copied from the private advanced recognition stack.

Notable OSS-original paths:

- `app/baseline/**`
- `app/main.py`
- `examples/local_demo.py`
- `tests/test_baseline_demo.py`
- `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `THIRD_PARTY_NOTICES.md`

`LICENSE` is the canonical GNU Affero General Public License version 3 text. `uv.lock` is generated dependency metadata. Empty package markers are OSS scaffolding and are not copied source.

## Deliberate exclusions

This release candidate excludes private Git history, SEEK-specific code, candidate/CV data, private prompts, advanced recognition and reranking heuristics, model weights, real screenshots, traces, runtime artifacts, and private historical documentation.
