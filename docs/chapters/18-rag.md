
# Capítulo 18 — RAG

## Objetivos

Construir o pipeline de recuperação e geração do PyTool, com citações e avaliação básica.

## Mentalidade Python

RAG é um pipeline: ingestão, recuperação, montagem de contexto, geração e avaliação. Não é uma caixa-preta “que sabe seus documentos”.

## Comparando com JavaScript

A arquitetura de pipeline é universal; Python oferece boa ergonomia para tratar dados, modelos e integrações em uma mesma aplicação.

## Conceitos

- Ingestão, retrieval, reranking e contexto.
- Grounding, citações e alucinação.
- Conjunto de avaliação representativo.

## 🧠 Como um Pythonista resolveria isso

Retorna fontes junto da resposta e mantém o pipeline separável para testar recuperação sem chamar um LLM.

## Implementação

Adicionar pergunta sobre documentos indexados, citando chunks usados e registrando a consulta.

## Engenharia

Avalie recuperação e geração separadamente; uma resposta ruim pode vir de qualquer etapa.

## ⚠️ Erros comuns

- Colocar documentos demais no contexto.
- Afirmar que RAG elimina alucinações.

## Exercícios

1. Criar três perguntas de avaliação com fonte esperada.
2. Implementar resposta quando não há contexto suficiente.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

RAG melhora fundamentação quando a recuperação, o contexto e a avaliação são tratados como componentes distintos.

## Checklist

- [ ] Respostas mostram fontes.
- [ ] Há conjunto mínimo de avaliação.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Material sobre avaliação de RAG.

## Ficha do capítulo

- **Capítulo:** 18
- **Dificuldade:** ⭐⭐⭐⭐☆
- **Duração estimada:** 120 minutos
- **Etapa do PyTool:** Respostas fundamentadas
- **Pré-requisitos:** Capítulo 17
- **Estado:** roteiro
