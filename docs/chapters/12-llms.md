
# Capítulo 12 — LLMs

## Objetivos

Criar uma abstração pequena para conversar com um modelo local ou remoto, sem começar por um framework de agentes.

## Mentalidade Python

Integre serviços por contratos estreitos. O modelo é uma dependência externa: pode falhar, ter latência, limites e respostas imperfeitas.

## Comparando com JavaScript

O padrão de cliente HTTP e objetos de configuração é familiar; Python adiciona protocolos e dataclasses para tornar substituições explícitas.

## Conceitos

- Mensagens, modelos de request/response e streaming.
- Cliente HTTP assíncrono.
- Credenciais por ambiente e timeouts.

## 🧠 Como um Pythonista resolveria isso

Define uma interface `ChatModel` e um adaptador por provedor, sem espalhar SDK de um fornecedor pelo domínio.

## Implementação

Adicionar ao PyTool um cliente de chat configurável para Ollama ou OpenAI e um comando de conversa simples.

## Engenharia

Logs devem registrar metadados úteis sem expor prompts sensíveis ou credenciais.

## ⚠️ Erros comuns

- Tratar saída do modelo como dado confiável.
- Colocar chaves de API no `pyproject.toml` ou no Git.

## Exercícios

1. Adicionar timeout e mensagem de falha amigável.
2. Criar fake de modelo para testes.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Um LLM é uma integração externa; contratos, timeouts e testes determinísticos vêm antes de “agência”.

## Leitura complementar

- Documentação do provedor escolhido.

## Ficha do capítulo

- **Capítulo:** 12
- **Dificuldade:** ⭐⭐⭐☆☆
- **Duração estimada:** 120 minutos
- **Etapa do PyTool:** Cliente de modelo
- **Pré-requisitos:** Capítulo 11
- **Explicação em poucas linhas:** Integração com LLMs via API, gerenciamento de chaves, tokens e streaming. O capítulo adiciona um cliente de modelo de linguagem ao PyTool.
