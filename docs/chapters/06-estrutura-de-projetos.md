
# Capítulo 6 — Estrutura de Projetos

## Objetivos

Organizar o PyTool por responsabilidades sem criar camadas antecipadas.

## Mentalidade Python

Pacotes devem refletir conceitos estáveis do domínio, não apenas categorias genéricas como `utils` ou `helpers`.

## Comparando com JavaScript

O layout `src/` evita imports acidentais da raiz; módulos Python são arquivos e pacotes, não uma árvore mediada por `node_modules`.

## Conceitos

- Pacotes, imports absolutos e públicos.
- Layout `src/`.
- Dependências direcionadas e fronteiras do domínio.

## 🧠 Como um Pythonista resolveria isso

Move funções por coesão de domínio, não por uma regra de “um arquivo por classe”.

## Implementação

Reorganizar a CLI, configuração e leitura de arquivos em módulos com APIs internas explícitas.

## Engenharia

Uma estrutura só ajuda se torna a navegação previsível e reduz acoplamento.

## ⚠️ Erros comuns

- Criar `utils.py` como destino de qualquer função sem dono.
- Expor detalhes internos através de `__init__.py` cedo demais.

## Exercícios

1. Justificar a posição de um módulo do PyTool.
2. Identificar uma dependência que aponta na direção errada.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Estrutura de projeto é uma ferramenta para preservar fronteiras e facilitar mudanças.

## Checklist

- [ ] Imports continuam funcionando após a reorganização.
- [ ] Testes não dependem de detalhes de CLI.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Guia de packaging Python.

## Ficha do capítulo

- **Capítulo:** 6
- **Dificuldade:** ⭐⭐☆☆☆
- **Duração estimada:** 60 minutos
- **Etapa do PyTool:** Pacote sustentável
- **Pré-requisitos:** Capítulo 5
- **Estado:** roteiro
