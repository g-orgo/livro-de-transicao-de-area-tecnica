# Apêndice B — Comandos do Ecossistema

Execute estes comandos na raiz de `project/pytool/`.

```powershell
uv init .
uv add NOME_DO_PACOTE
uv add --dev NOME_DO_PACOTE
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run ruff format .
```

| Comando | Efeito |
|---|---|
| `uv init .` | Cria ou inicializa metadados do projeto atual. |
| `uv add` | Declara e instala uma dependência. |
| `uv sync` | Sincroniza o ambiente com metadados e lockfile. |
| `uv run` | Executa comando no ambiente virtual do projeto. |
| `ruff check .` | Analisa problemas de lint. |
| `ruff format --check .` | Confere formatação sem modificar arquivos. |
| `pytest` | Descobre e executa testes. |

Versione `pyproject.toml` e `uv.lock`. Não versione `.venv/`.
