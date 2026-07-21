
# Capítulo 8 — Testes

## Objetivos

Usar pytest, fixtures, parametrização e mocks para testar o PyTool sem acoplar testes à implementação.

## Mentalidade Python

Teste comportamento observável. Fixtures são composição explícita de contexto, não apenas “setup”.

## Comparando com JavaScript

pytest descobre funções de teste por convenção; fixtures injetadas por argumento substituem parte do ciclo `beforeEach` de Jest/Vitest.

## Conceitos

- Arrange, act, assert.
- Fixtures e `tmp_path`.
- Parametrização, exceções e mocks na fronteira.

## 🧠 Como um Pythonista resolveria isso

Usa `tmp_path` para criar arquivos reais temporários em vez de mockar `pathlib` por padrão.

## Implementação

Cobrir configuração, leitura de arquivos e comandos do PyTool; adicionar uma base de testes de regressão.

## Engenharia

Testes rápidos e determinísticos tornam refatoração uma ação segura, não uma aposta.

## ⚠️ Erros comuns

- Mockar toda colaboração interna.
- Testar nomes privados em vez de resultado público.

## Exercícios

1. Parametrizar extensões aceitas.
2. Criar teste para caminho inexistente.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Pytest favorece testes pequenos e composição de contexto por fixtures.

## Leitura complementar

- Documentação do pytest.

## Ficha do capítulo

- **Capítulo:** 8
- **Dificuldade:** ⭐⭐☆☆☆
- **Duração estimada:** 90 minutos
- **Etapa do PyTool:** Confiança para evoluir
- **Pré-requisitos:** Capítulo 7
- **Explicação em poucas linhas:** pytest fixtures, parametrização, monkeypatch e boas práticas de teste. O capítulo constrói confiança para evoluir o PyTool com segurança.
