
# Capítulo 4 — Objetos em Python

## Objetivos

Modelar a configuração do PyTool com dataclasses, composição e protocolos leves.

## Mentalidade Python

Classes existem para representar comportamento e estado coesos, não como uma exigência para toda função ou dado.

## Comparando com JavaScript

`@dataclass` substitui muito boilerplate de construtores; `Protocol` oferece tipagem estrutural onde TypeScript frequentemente usa interfaces.

## Conceitos

- Classes, instâncias e atributos.
- Dataclasses, imutabilidade e `default_factory`.
- Composição, ABC e `Protocol`.

## 🧠 Como um Pythonista resolveria isso

Usa uma dataclass pequena para opções de configuração e funções para transformações puras, em vez de uma classe de serviço genérica.

## Implementação

Ler configuração do PyTool, aplicar valores padrão e separar fonte da configuração de seu modelo.

## Engenharia

Modelos pequenos e explícitos tornam validação, testes e refatoração mais baratos.

## ⚠️ Erros comuns

- Usar uma lista como default mutável em dataclass.
- Construir heranças profundas para reutilização superficial.

## Exercícios

1. Adicionar diretório de trabalho à configuração.
2. Criar um adaptador de configuração em memória para testes.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Dataclasses e composição costumam ser o ponto de partida mais claro para objetos em Python.

## Checklist

- [ ] Configuração possui defaults testados.
- [ ] Nenhum default mutável é compartilhado.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Documentação: `dataclasses` e `typing.Protocol`.

## Ficha do capítulo

- **Capítulo:** 4
- **Dificuldade:** ⭐⭐☆☆☆
- **Duração estimada:** 75 minutos
- **Etapa do PyTool:** Configuração
- **Pré-requisitos:** Capítulo 3
- **Estado:** roteiro
