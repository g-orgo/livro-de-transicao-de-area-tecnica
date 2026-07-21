
# Capítulo 15 — Tool Calling

## Objetivos

Permitir que o PyTool execute ferramentas declaradas pelo modelo sob validação e limites explícitos.

## Mentalidade Python

O modelo sugere uma chamada; a aplicação autoriza, valida e executa. Nunca entregue capacidade irrestrita a texto gerado.

## Comparando com JavaScript

O padrão se parece com registrar handlers em uma tabela; protocolos e modelos tipados tornam o contrato explícito.

## Conceitos

- Esquema de ferramenta, argumentos e resultado.
- Loop de ferramenta e limite de iterações.
- Autorização e observabilidade.

## 🧠 Como um Pythonista resolveria isso

Usa registro explícito de ferramentas com funções pequenas, em vez de executar código ou comandos construídos pelo LLM.

## Implementação

Expor ferramentas seguras para listar arquivos e consultar histórico; registrar cada chamada.

## Engenharia

Ferramentas são fronteiras de segurança. Entrada do modelo é sempre não confiável.

## ⚠️ Erros comuns

- Fazer `eval` ou executar shell a partir de saída do modelo.
- Não limitar chamadas repetidas.

## Exercícios

1. Rejeitar argumento fora do diretório permitido.
2. Criar ferramenta somente leitura e testá-la.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

Tool calling é integração controlada, não autonomia sem limites.

## Checklist

- [ ] Ferramentas têm esquema e testes.
- [ ] Chamadas são limitadas e registradas.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- Documentação de function calling do provedor.

## Ficha do capítulo

- **Capítulo:** 15
- **Dificuldade:** ⭐⭐⭐⭐☆
- **Duração estimada:** 120 minutos
- **Etapa do PyTool:** Ações controladas
- **Pré-requisitos:** Capítulo 14
- **Estado:** roteiro
