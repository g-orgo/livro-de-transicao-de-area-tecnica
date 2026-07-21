
# Capítulo 10 — Banco de Dados

## Objetivos

Persistir histórico e configurações com SQLite, SQLAlchemy e migrações controladas.

## Mentalidade Python

ORM é uma camada de mapeamento, não uma desculpa para esquecer que há SQL, transações e índices.

## Comparando com JavaScript

SQLAlchemy separa modelos, sessões e expressões de consulta; não assume o mesmo padrão ativo de todos os ORMs Node.

## Conceitos

- SQLite, conexão, sessão e transação.
- Modelos SQLAlchemy e repositórios pequenos.
- Migrações Alembic.

## 🧠 Como um Pythonista resolveria isso

Delimita a transação na fronteira da operação e evita propagar uma sessão global pelo sistema.

## Implementação

Persistir execuções do PyTool e recuperar o histórico pelo CLI.

## Engenharia

Banco de dados é uma dependência externa: testes precisam de isolamento e migrações precisam ser versionadas.

## ⚠️ Erros comuns

- Consultar dentro de loops sem perceber o custo.
- Usar a sessão como singleton de aplicação.

## Exercícios

1. Filtrar histórico por tipo de comando.
2. Criar uma migração para campo adicional.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Persistência exige limites explícitos de transação e evolução versionada de esquema.

## Checklist

- [ ] Migração cria o esquema local.
- [ ] Histórico é persistido e lido.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Documentação de SQLAlchemy e Alembic.

## Ficha do capítulo

- **Capítulo:** 10
- **Dificuldade:** ⭐⭐⭐☆☆
- **Duração estimada:** 120 minutos
- **Etapa do PyTool:** Persistência
- **Pré-requisitos:** Capítulo 9
- **Estado:** roteiro
