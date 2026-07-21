
# Capítulo 9 — CLI Profissional

## Objetivos

Construir uma interface de terminal utilizável com Typer e saída legível com Rich.

## Mentalidade Python

Uma CLI é uma interface pública: comandos, argumentos, mensagens de erro e códigos de saída são contratos.

## Comparando com JavaScript

Typer usa type hints para declarar argumentos, aproximando a assinatura da função da documentação e da validação do CLI.

## Conceitos

- Comandos, argumentos, opções e códigos de saída.
- Typer e Rich.
- Separação entre adaptador de CLI e lógica de aplicação.

## 🧠 Como um Pythonista resolveria isso

Mantém a função de domínio independente de Typer para testá-la sem simular um terminal.

## Implementação

Substituir a CLI mínima por comandos `version`, `files` e `config`, com ajuda automática e saída formatada.

## Engenharia

Interfaces de terminal previsíveis permitem automação e evitam que mensagens humanas virem APIs acidentais.

## ⚠️ Erros comuns

- Misturar parse de argumentos e regra de negócio.
- Imprimir erros sem definir código de saída.

## Exercícios

1. Adicionar opção `--json`.
2. Definir um código de saída para diretório inválido.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Typer e Rich melhoram ergonomia, mas a lógica deve continuar independente do terminal.

## Checklist

- [ ] `pytool --help` explica os comandos.
- [ ] A CLI tem testes de comportamento.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Documentação de Typer e Rich.

## Ficha do capítulo

- **Capítulo:** 9
- **Dificuldade:** ⭐⭐☆☆☆
- **Duração estimada:** 90 minutos
- **Etapa do PyTool:** Interface de terminal
- **Pré-requisitos:** Capítulo 8
- **Estado:** roteiro
