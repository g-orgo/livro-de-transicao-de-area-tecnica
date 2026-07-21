
# Capítulo 14 — Memória

## Objetivos

Separar contexto de conversa, histórico persistido e conhecimento recuperável.

## Mentalidade Python

“Memória” não é um recurso único: cada tipo tem custo, duração, privacidade e política de recuperação próprios.

## Comparando com JavaScript

Modelagem e persistência são equivalentes conceituais; a diferença vem das dataclasses, Pydantic e sessão de banco já presentes no PyTool.

## Conceitos

- Memória de curto e longo prazo.
- Janela de contexto, resumo e retenção.
- Identidade de conversa e privacidade.

## 🧠 Como um Pythonista resolveria isso

Modela mensagens persistidas e uma política de seleção de contexto separadamente do cliente LLM.

## Implementação

Persistir sessões, reconstituir contexto limitado e permitir iniciar uma conversa nova.

## Engenharia

Políticas de retenção devem ser explícitas antes que dados reais de usuários sejam armazenados.

## ⚠️ Erros comuns

- Enviar todo o histórico para sempre.
- Chamar qualquer armazenamento vetorial de “memória”.

## Exercícios

1. Limitar contexto por número de mensagens.
2. Criar teste para isolamento de sessões.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Memória é modelagem de dados e política de contexto, não uma lista global de mensagens.

## Leitura complementar

- Material sobre context windows do provedor escolhido.

## Ficha do capítulo

- **Capítulo:** 14
- **Dificuldade:** ⭐⭐⭐☆☆
- **Duração estimada:** 90 minutos
- **Etapa do PyTool:** Conversas persistentes
- **Pré-requisitos:** Capítulo 13
- **Explicação em poucas linhas:** Memória conversacional, histórico, sumarização e armazenamento persistente de contexto. O capítulo torna as interações do PyTool com LLMs mais coerentes.
