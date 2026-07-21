# Apêndice A — Python × JavaScript

| Conceito | JavaScript / TypeScript | Python |
|---|---|---|
| Ausência de valor | `null`, `undefined` | `None` |
| Função | `function` / arrow function | `def` |
| Classe de dados | objeto literal / interface | `@dataclass` / Pydantic |
| Dependências | `package.json` | `pyproject.toml` |
| Ambiente local | `node_modules` | `.venv` |
| Teste | Jest/Vitest | pytest |
| Lint/format | ESLint/Prettier | Ruff |
| Interface estrutural | `interface` | `Protocol` |
| Async | `async` / `await` | `async` / `await` |
| Caminhos | `path` | `pathlib.Path` |

## Diferenças que importam

- Python usa indentação para blocos; chaves não existem.
- Nomes de módulo e função normalmente usam `snake_case`; classes usam `PascalCase`.
- Coleções vazias são falsas: `if items:` costuma ser preferível a `if len(items) > 0:`.
- `is` compara identidade; para valores use `==`, exceto `value is None`.
- Type hints são opcionais em runtime e não validam dados por si só.

Use esta tabela como ponte, não como uma tradução perfeita entre linguagens.
