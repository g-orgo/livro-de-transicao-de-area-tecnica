
# Capítulo 13 — Prompts

## Objetivos

Tratar prompts como ativos versionados, testáveis e separados da lógica de transporte do modelo.

## Mentalidade Python

Um prompt é parte do comportamento do produto. Deve ter nome, contexto de uso e uma forma de ser revisado.

## Comparando com JavaScript

Arquivos de template e modelos tipados cumprem papel semelhante a templates e schemas em aplicações TypeScript.

## Conceitos

- System prompt, contexto, few-shot e templates.
- Separação de conteúdo e interpolação.
- Testes de estrutura, não de criatividade do modelo.

## 🧠 Como um Pythonista resolveria isso

Carrega um template nomeado e fornece dados explícitos, em vez de concatenar strings em handlers de CLI ou API.

## Implementação

Criar diretório de prompts e um renderizador para o comando de chat do PyTool.

## Engenharia

Versionar prompts permite revisar mudanças comportamentais no mesmo fluxo do código.

## ⚠️ Erros comuns

- Interpolar dados não confiáveis sem delimitação.
- Confundir teste de template com avaliação de qualidade do modelo.

## Exercícios

1. Criar prompt especializado para resumir arquivo.
2. Testar campos obrigatórios do template.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Prompts são interfaces de produto e merecem versionamento e revisão.

## Checklist

- [ ] Prompts não estão embutidos no transporte HTTP.
- [ ] Template possui teste de renderização.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Guia do provedor sobre prompting.

## Ficha do capítulo

- **Capítulo:** 13
- **Dificuldade:** ⭐⭐☆☆☆
- **Duração estimada:** 75 minutos
- **Etapa do PyTool:** Prompts versionados
- **Pré-requisitos:** Capítulo 12
- **Estado:** roteiro
