
# Capítulo 7 — Tipagem

## Objetivos

Aplicar anotações úteis no PyTool e distinguir tipagem estática de validação em runtime.

## Mentalidade Python

Tipos documentam contratos e ampliam o feedback do editor; não substituem testes nem tornam Python estaticamente tipado em runtime.

## Comparando com JavaScript

Type hints se aproximam de TypeScript, mas são opcionais e nativos da linguagem; `Protocol` tipa comportamento estrutural.

## Conceitos

- `list[str]`, `dict[str, str]`, unions e `None`.
- `TypeAlias`, `Literal`, `Annotated`, generics e `Protocol`.
- Pyright/ty como análise estática; Pydantic como validação posterior.

## 🧠 Como um Pythonista resolveria isso

Anota uma fronteira pública e deixa detalhes locais óbvios sem poluir todo valor com tipos redundantes.

## Implementação

Tipar APIs públicas do PyTool, resultados de busca de arquivos e contrato de plugin.

## Engenharia

A maior vantagem aparece nas fronteiras: I/O, configurações, plugins e respostas externas.

## ⚠️ Erros comuns

- Usar `Any` para silenciar problemas.
- Confundir anotação com conversão de valor em runtime.

## Exercícios

1. Criar um `Protocol` para uma fonte de configuração.
2. Substituir um retorno ambíguo por um tipo explícito.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Tipagem é um contrato gradual, mais valioso em interfaces do que em cerimônia local.

## Leitura complementar

- Documentação: `typing`.

## Ficha do capítulo

- **Capítulo:** 7
- **Dificuldade:** ⭐⭐⭐☆☆
- **Duração estimada:** 90 minutos
- **Etapa do PyTool:** Contratos explícitos
- **Pré-requisitos:** Capítulo 6
- **Explicação em poucas linhas:** Type hints, tipagem estrutural vs nominal e como tipos funcionam como documentação executável. O capítulo adiciona contratos explícitos ao PyTool.
