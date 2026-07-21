---
name: validate-exercises
description: Use when the user explicitly cites a chapter number to validate "R:" answers. Ignores vague review requests like "corrige", "valida", "confere", "review my answers" without a specific chapter.
---

# Skill: validate-exercises

Valida respostas de exercícios em UM capítulo específico da documentação (`docs/chapters/*.md`).

## Regras

0. **O usuário DEVE informar qual capítulo validar** (ex.: "capítulo 1", "cap 5", "chapter 3", "01", "validate 07"). Se não houver indicação explícita de capítulo, não fazer nada — ignorar o pedido.
1. **NÃO alterar o conteúdo original das respostas.** A resposta do usuário é preservada.
2. **NÃO corrigir gramática, ortografia ou estilo de redação.** O foco é o entendimento conceitual.
3. **Apenas marcar** a linha `R:` com um emoji prefixado:
   - `✅` — resposta correta dentro do contexto do capítulo (mesmo que redigida de forma diferente — o conceito estar correto basta)
   - `⚠️` — resposta com erro conceitual grave que contradiz o que o capítulo ensina; após o `R:` adicione um breve comentário entre colchetes com o que precisa ajustar
4. **Dialogar com o usuário** explicando por que algo está errado quando marcar com `⚠️`, de forma aberta a discussão.
5. **Processar TODOS os `R:` do arquivo**, não apenas o primeiro.
6. **Se não houver `R:` no arquivo**, informar o usuário.

## Formato de marcação

**Correta:**
```markdown
✅ R: resposta
```

**Com alerta:**
```markdown
⚠️ R: [ajuste: explicar o problema conceitual] resposta original
```

## Critérios de avaliação

- **Erro conceitual** = contradiz diretamente o capítulo. Ex: dizer que `.venv` = `pyproject.toml`.
- **Não é erro conceitual:** redação diferente, sinônimos, explicação mais abrangente, analogias próprias, erros de português, omissão de detalhes não essenciais.
- Aceite respostas que cheguem no mesmo destino por caminho diferente.
- Na dúvida entre ✅ e ⚠️, prefira ✅ e pergunte ao usuário se quer aprofundar.
