# Apêndice C — Erros Frequentes de quem vem de JavaScript

| Hábito | Alternativa Pythonica | Motivo |
|---|---|---|
| `for i in range(len(items))` | `for item in items` | Elimina índice quando ele não importa. |
| `if len(items) > 0` | `if items` | Coleções vazias são falsas. |
| `if flag == True` | `if flag` | A intenção fica mais direta. |
| usar `list` como variável | escolher `items`, `values` | Não sombreia built-ins. |
| `open(...)` sem fechamento | `with open(...) as file` | Fecha o recurso mesmo em exceções. |
| caminhos como string | `Path` | Evita concatenação dependente de plataforma. |
| classes para tudo | função ou dataclass | Menos cerimônia e acoplamento. |
| `is` para string/número | `==` | `is` verifica identidade. |

Essas regras não são dogmas. Elas são boas escolhas padrão até que o contexto peça algo diferente.
