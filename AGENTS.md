# AGENTS.md — Python para Engenheiros JavaScript

## Repo structure

- `docs/` — book chapters (Markdown, one per chapter, 00-20)
- `project/pytool/` — the PyTool project (Python package, `src` layout)
- All development commands run from `project/pytool/`

## Toolchain

| Tool     | Role              | Config location                          |
| -------- | ----------------- | ---------------------------------------- |
| **uv**   | Project manager   | `pyproject.toml` + `uv.lock`             |
| **Ruff** | Linter + formatter| `[tool.ruff]` in `pyproject.toml`        |
| **pytest**| Test runner       | `[tool.pytest.ini_options]` in `pyproject.toml` |

- Python 3.14 (`.python-version`)
- Ruff line length: 88, target: py312

## Commands (always run from `project/pytool/`)

```powershell
uv run pytest              # run all tests
uv run ruff check          # lint
uv run ruff format         # auto-format
```

## Quirks

- **`testpaths = ["tests"]` in pyproject.toml is stale.** Actual tests are in `src/tests/`. pytest still discovers them with a warning. Fixing `testpaths` to `["src/tests"]` removes the warning.
- **No `.gitignore`** exists at the repo or project root (only the auto-generated one inside `.venv/`).
- **No type checker** (mypy/pyright) is configured.
- **No CI, pre-commit, or task runner** — only manual `uv run` commands.
