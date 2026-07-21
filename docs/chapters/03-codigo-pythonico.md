
# Capítulo 3 — Escrevendo Código Pythonico

## Objetivos

Usar iteração direta, `enumerate`, `zip`, compreensões, `any`, `all`, geradores e `pathlib` para listar arquivos no PyTool.

## Mentalidade Python

Itere sobre valores quando o índice não importa. Prefira uma expressão clara a uma sequência de mutações intermediárias.

## Comparando com JavaScript

`for item in items` substitui laços indexados; list comprehensions frequentemente substituem `filter().map()`; `pathlib.Path` substitui boa parte de `path` e `fs`.

## Conceitos

- Protocolo de iteração e lazy evaluation.
- Compreensões e quando uma função nomeada é mais legível.
- `Path.iterdir`, `glob` e `rglob`.

## 🧠 Como um Pythonista resolveria isso

Usa `for index, file in enumerate(files, start=1)` quando precisa de posição, nunca `range(len(files))` sem necessidade.

## Implementação

Criar `pytool files PATH`, filtrando extensões e retornando saída determinística.

## Engenharia

Aceitar `Path` na lógica interna reduz acoplamento ao terminal e facilita testes com diretórios temporários.

## ⚠️ Erros comuns

- Converter todo iterável em lista antes de precisar.
- Usar strings para montar caminhos.

## Exercícios

1. Adicionar filtro por extensão.
2. Exibir a contagem total sem fazer uma segunda varredura desnecessária.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Python oferece abstrações de iteração que removem índices, mutação e caminhos manuais do código cotidiano.

## Checklist

- [ ] `files PATH` funciona com `Path`.
- [ ] Resultados têm ordem definida.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Documentação: `pathlib` e `itertools`.

## Ficha do capítulo

- **Capítulo:** 3
- **Dificuldade:** ⭐⭐☆☆☆
- **Duração estimada:** 75 minutos
- **Etapa do PyTool:** Leitura de arquivos
- **Pré-requisitos:** Capítulo 2
- **Estado:** roteiro
