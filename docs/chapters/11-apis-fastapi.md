
# Capítulo 11 — APIs com FastAPI

## Objetivos

Expor capacidades do PyTool por HTTP com FastAPI, Pydantic e dependências explícitas.

## Mentalidade Python

Uma API é uma fronteira: converte entrada externa em modelos internos e nunca deve vazar detalhes de persistência por acidente.

## Comparando com JavaScript

FastAPI deriva validação e documentação de assinaturas tipadas; Pydantic valida dados em runtime, função parecida com Zod em muitos projetos TypeScript.

## Conceitos

- Rotas, modelos Pydantic e status HTTP.
- Dependency injection do FastAPI.
- Tratamento de erro e streaming.

## 🧠 Como um Pythonista resolveria isso

Usa dependências do framework para construir recursos por requisição em vez de importar singletons globais no handler.

## Implementação

Criar endpoints para arquivos, configuração e histórico; manter o núcleo reutilizável pela CLI.

## Engenharia

CLI e API são adaptadores sobre os mesmos casos de uso, e não dois produtos com lógica duplicada.

## ⚠️ Erros comuns

- Retornar modelos de banco diretamente.
- Marcar uma rota como `async` sem entender as dependências chamadas.

## Exercícios

1. Adicionar endpoint paginado de histórico.
2. Converter erro de domínio em resposta HTTP estável.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

FastAPI torna contratos explícitos, mas arquitetura continua responsabilidade do projeto.

## Leitura complementar

- Documentação do FastAPI.

## Ficha do capítulo

- **Capítulo:** 11
- **Dificuldade:** ⭐⭐⭐☆☆
- **Duração estimada:** 120 minutos
- **Etapa do PyTool:** API HTTP
- **Pré-requisitos:** Capítulo 10
- **Explicação em poucas linhas:** Criação de APIs HTTP com FastAPI, rotas, validação com Pydantic e documentação automática. O capítulo expõe o PyTool como serviço web.
