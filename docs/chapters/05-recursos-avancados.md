
# Capítulo 5 — Recursos Avançados da Linguagem

## Objetivos

Entender decorators, context managers, properties e dunder methods por meio de um mecanismo pequeno de extensões do PyTool.

## Mentalidade Python

Recursos avançados devem tornar uma intenção repetida mais clara. Não são uma licença para abstração mágica.

## Comparando com JavaScript

Decorators existem em ambos os ecossistemas, mas context managers (`with`) têm um papel central no gerenciamento determinístico de recursos Python.

## Conceitos

- Funções como valores e closures.
- Decorators e metadados preservados.
- Context managers e `__enter__`/`__exit__`.
- Properties e representações `__repr__`.

## 🧠 Como um Pythonista resolveria isso

Usa `with` para garantir fechamento de recursos, em vez de depender de um `finally` espalhado pela chamada.

## Implementação

Registrar comandos extensíveis e criar um context manager para uma sessão de execução do PyTool.

## Engenharia

Uma extensão só é útil quando possui contrato explícito, ciclo de vida claro e falhas observáveis.

## ⚠️ Erros comuns

- Empilhar decorators sem conseguir explicar sua ordem.
- Usar mágicas de dunder methods para esconder comportamento importante.

## Exercícios

1. Criar um decorator que registra duração de uma função.
2. Implementar `__repr__` útil para a configuração.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Recursos avançados valem quando clarificam gerenciamento de recursos ou contratos repetidos.

## Leitura complementar

- PEP 343 — The `with` statement.

## Ficha do capítulo

- **Capítulo:** 5
- **Dificuldade:** ⭐⭐⭐☆☆
- **Duração estimada:** 90 minutos
- **Etapa do PyTool:** Plugins mínimos
- **Pré-requisitos:** Capítulo 4
- **Explicação em poucas linhas:** Decoradores, context managers e metaprogramação permitem código expressivo e enxuto. O capítulo prepara a base para plugins e extensibilidade no PyTool.
