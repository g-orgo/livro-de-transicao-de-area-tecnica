
# Capítulo 2 — A Sintaxe Essencial

## Objetivos

Usar módulos, imports, funções, anotações básicas, coleções e exceções para transformar o PyTool em uma CLI mínima.

## Mentalidade Python

Python usa blocos por indentação e favorece funções pequenas, módulos explícitos e valores simples antes de criar hierarquias de classes.

## Comparando com JavaScript

`def`, `None`, `str | None`, `list[str]`, `raise` e imports por módulo substituem equivalentes de funções, `null`/`undefined`, unions TypeScript, arrays, `throw` e módulos ES.

## Conceitos

- Variáveis não têm declaração; valores têm tipos.
- Funções, argumentos nomeados e retorno.
- `list`, `dict`, `tuple`, `set` e `None`.
- Módulos, `__init__.py` e exceções.

## 🧠 Como um Pythonista resolveria isso

Prefere `def format_message(name: str) -> str` a uma classe com um único método estático.

## Implementação

Adicionar o comando `pytool --version`, uma função de apresentação e testes para saída e erros de entrada.

## Engenharia

Separar a lógica que calcula um valor da camada que imprime no terminal simplifica testes.

## ⚠️ Erros comuns

- Usar `{}` esperando um objeto: em Python cria um `dict`.
- Usar `is` para comparar strings.
- Criar classes apenas para agrupar funções.

## Exercícios

1. Implementar `pytool greet NOME`.
2. Explicar a diferença entre `None` e uma string vazia.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Funções, módulos e valores simples resolvem a maior parte do primeiro incremento do PyTool.

## Checklist

- [ ] CLI imprime a versão.
- [ ] Testes cobrem a lógica de apresentação.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Tutorial oficial: módulos e funções.

## Ficha do capítulo

- **Capítulo:** 2
- **Dificuldade:** ⭐☆☆☆☆
- **Duração estimada:** 60 minutos
- **Etapa do PyTool:** Primeiro comando
- **Pré-requisitos:** Capítulo 1
- **Estado:** roteiro
