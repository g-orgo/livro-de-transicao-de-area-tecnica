# Python para Engenheiros JavaScript

> Construindo software moderno e um agente de IA enquanto aprende Python.

Este é um **livro vivo** para quem já programa em JavaScript e quer adquirir fluência em Python sem repetir uma introdução à lógica de programação. A meta é aprender o modo Python de projetar, ler e manter software enquanto o **PyTool** evolui de uma CLI pequena para uma plataforma de IA.

## Como usar este livro

1. Abra [SUMMARY.md](SUMMARY.md) e siga os capítulos em ordem.
2. Leia o objetivo e faça a entrega prática antes de seguir para o próximo capítulo.
3. Use os exercícios como pausas de aprendizagem. Você pode respondê-los mentalmente, em um caderno ou no código; não é necessário enviar respostas nem registrá-las para revisão.
4. Use os apêndices como referência rápida, sem tentar decorá-los.

Cada capítulo se fecha com um pequeno resultado verificável. Não avance apenas porque leu: avance quando conseguir explicar a decisão e verificar o resultado localmente.

## Convenções

- Todos os documentos usam UTF-8 e Markdown comum.
- Trechos marcados como `Path:` indicam o caminho relativo à raiz deste repositório.
- `🧠 Como um Pythonista resolveria` compara uma solução que vem naturalmente do JavaScript com uma solução idiomática em Python.
- `⚠️ Erro comum` destaca hábitos que produzem código correto, porém pouco idiomático ou frágil.
- A **Ficha do capítulo**, no fim de cada arquivo, reúne número, dificuldade, duração, etapa do PyTool, pré-requisitos e estado. Assim, a leitura começa diretamente pelo conteúdo.
- Os capítulos em estado **roteiro** têm a sequência, a entrega e os exercícios definidos; eles se tornam aulas completas quando chegarmos neles.

## O projeto contínuo: PyTool

O PyTool começa como uma ferramenta de terminal para desenvolvedores. A progressão é deliberada:

```text
CLI → arquivos e configuração → HTTP e async → persistência e API
→ LLMs e memória → ferramentas e MCP → embeddings e RAG → entrega
```

O código do projeto fica em [`project/pytool/`](project/pytool/). No Capítulo 1 ele ainda é só um ambiente profissional mínimo; cada capítulo seguinte adicionará uma capacidade pequena e testável.

## Pré-requisitos

- Python e VS Code já instalados.
- Familiaridade com terminal, Git, HTTP e JavaScript/TypeScript.
- `uv` será usado como gerenciador de projeto; o Capítulo 1 ensina a confirmar sua disponibilidade e criar o projeto.

## Estado atual

O próximo passo é o [Capítulo 1 — Um Ambiente Profissional](chapters/01-ambiente-profissional.md), começando pelo Exercício 1.1 e pela criação do ambiente do PyTool.
