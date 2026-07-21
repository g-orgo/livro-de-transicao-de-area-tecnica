
# Capítulo 1 — Um Ambiente Profissional

## Objetivos

Ao terminar, você conseguirá explicar o que um ambiente virtual isola, ler os elementos essenciais de um `pyproject.toml` e criar um PyTool mínimo com dependências, lint, formatação e testes reproduzíveis.

## Mentalidade Python

O projeto é mais importante que a máquina. O objetivo não é “fazer funcionar no meu computador”, e sim definir um ambiente que qualquer pessoa possa reconstruir. Em Python, isso combina três peças: uma versão compatível do interpretador, dependências declaradas e um ambiente virtual isolado.

O ambiente virtual não contém uma cópia do seu código nem é o equivalente exato de `node_modules`. Ele é um conjunto isolado de pacotes Python e scripts associados a um interpretador. Dependências continuam sendo declaradas no projeto; o ambiente é apenas a instalação local delas.

## Comparando com JavaScript

| Problema | JavaScript/Node | Python moderno |
|---|---|---|
| Metadados do projeto | `package.json` | `pyproject.toml` |
| Dependências | `npm install` | `uv add` / `uv sync` |
| Instalação isolada | `node_modules` | `.venv` |
| Lockfile | `package-lock.json` / `pnpm-lock.yaml` | `uv.lock` |
| Linter e formatter | ESLint + Prettier | Ruff |
| Testes | Jest / Vitest | pytest |

## Conceitos

### Ambiente virtual

Instalar pacotes globalmente cria uma fonte compartilhada de conflitos: o Projeto A pode exigir uma versão diferente daquela que o Projeto B exige. Um `.venv` evita que instalar uma biblioteca para o PyTool altere outros projetos ou o Python global.

### `pyproject.toml`

Este arquivo descreve o projeto e concentra a configuração das ferramentas. É o equivalente conceitual mais próximo de um `package.json`, embora use TOML e siga padrões do ecossistema Python. Ele deve ser versionado.

### `uv`, Ruff e pytest

- **uv** cria o projeto, resolve dependências, mantém o lockfile e executa comandos no ambiente virtual correto.
- **Ruff** é linter e formatter rápido. Seu trabalho é apontar problemas de estilo e aplicar um formato consistente.
- **pytest** descobre e executa testes usando convenções simples: arquivos `test_*.py` e funções `test_*`.

## 🧠 Como um Pythonista resolveria isso

**Problema:** garantir que uma colega execute o PyTool com as mesmas dependências.

Uma abordagem improvisada seria listar comandos soltos em um README, instalar bibliotecas globalmente e torcer para que as versões coincidam.

Uma abordagem Pythonica é declarar a intenção no `pyproject.toml`, registrar a resolução exata no `uv.lock` e pedir que a colega execute `uv sync`. O repositório passa a ser a fonte de verdade; a máquina local é apenas uma reprodução dele.

## Implementação

### 1. Confirme o `uv`

No terminal aberto na raiz deste repositório, execute:

```powershell
uv --version
```

Você deve ver uma versão. Se o comando não for reconhecido, pare aqui: precisamos instalar o `uv` antes de continuar. Não substitua os comandos por `pip` nesta trilha, pois o objetivo do capítulo é justamente aprender o fluxo com `uv`.

### 2. Crie o projeto

Execute:

```powershell
uv init --package project/pytool
cd project/pytool
uv add --dev ruff pytest
```

Isso cria `pyproject.toml`, `README.md`, `.python-version`, `uv.lock` e o ambiente `.venv` quando necessário. A opção `--dev` indica que Ruff e pytest são ferramentas de desenvolvimento, não bibliotecas exigidas para usar o PyTool em produção.

### 3. Declare a versão e as ferramentas

Substitua o conteúdo do arquivo abaixo pelo bloco completo. A versão `>=3.12` é uma escolha didática para usar recursos modernos com boa legibilidade; use uma versão posterior se o `uv` informar que a sua não é compatível.

Path: `project/pytool/pyproject.toml`

```toml
[project]
name = "pytool"
version = "0.1.0"
description = "Ferramenta para desenvolvedores construída durante o livro Python para Engenheiros JavaScript."
readme = "README.md"
requires-python = ">=3.12"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[dependency-groups]
dev = [
  "pytest>=8.0",
  "ruff>=0.9",
]

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

`[project]` descreve o pacote; `[dependency-groups]` separa ferramentas de desenvolvimento; as duas seções `tool` configuram as convenções que vamos usar em todos os capítulos.

### 4. Crie uma primeira unidade de código e um teste

Crie as pastas `src/pytool` e `tests`. Depois crie os dois arquivos abaixo.

Path: `project/pytool/src/pytool/__init__.py`

```python
"""Pacote principal do PyTool."""
```

Path: `project/pytool/src/pytool/version.py`

```python
def current_version() -> str:
    """Return the version displayed by the first PyTool command."""
    return "0.1.0"
```

Path: `project/pytool/tests/test_version.py`

```python
from pytool.version import current_version


def test_current_version() -> None:
    assert current_version() == "0.1.0"
```

O código é propositalmente pequeno: ele prova que a estrutura `src/`, o import e o pytest funcionam antes de colocarmos uma CLI em cima dela.

### 5. Sincronize e verifique

O `uv init --package` e a seção `[build-system]` permitem que o projeto seja instalado no ambiente em modo de desenvolvimento. Em seguida, execute:

```powershell
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Resultado esperado: Ruff não reporta violações, o formatter não pede mudanças e pytest encerra com `1 passed`. Se o formatter pedir mudanças, rode `uv run ruff format .`, releia o diff e repita a verificação.

## Engenharia

A estrutura `src/` impede que testes importem acidentalmente o código diretamente da raiz do repositório. Isso torna a instalação do pacote parte do fluxo normal, aproximando o desenvolvimento da forma como usuários e integração contínua consumirão o projeto.

Em projetos reais, versione `pyproject.toml` e `uv.lock`; ignore `.venv`. O lockfile oferece reprodutibilidade. O ambiente virtual é um detalhe local e recriável.

## ⚠️ Erros comuns

- Instalar pacotes com `pip` globalmente “só desta vez”.
- Versionar `.venv/`.
- Usar `ruff format .` sem revisar a alteração quando o formatter corrige um arquivo inesperado.
- Confundir o Python ativo no terminal com o Python isolado que `uv run` escolhe para o projeto.
- Trocar ferramentas no meio da trilha sem um problema concreto a resolver.

## Exercícios

### Exercício 1.1 — Modelo mental

Responda, em suas palavras:

1. Por que instalar bibliotecas globalmente pode causar problemas?
R: Porquê pode conflitar com depedências nativas do Python assim como com de outros projetos.
2. Em que isso se parece com projetos Node.js?
R: Utiliza uma estrutura similar de gerenciamento de pacotes e de comandos para geração de blocos de configuração e estruturas padronizadas.
3. Qual é a diferença prática entre `.venv` e `node_modules`?
R: `node_modules` contem uma cópia de todo o ecossistema das depedencias portanto é extremamente "maior" no sentido de quantidade de pacotes/arquivos e não lida diretamente com a interpretação destes dados e sim com a disponibilidade deles; já no caso do .venv ele atua como um ambiente inteiro dedicado àquelas dependências responsável por orquestrar, rodar e disponibilizar dependências.

### Exercício 1.2 — Verificação consciente

Sem consultar a resposta, explique o que cada comando faz: `uv sync`, `uv run ruff check .` e `uv run pytest`.

## Prática pessoal

Os exercícios deste capítulo são pausas de aprendizagem: responda mentalmente, em um caderno ou diretamente no código quando a atividade for prática. Todas as informações necessárias para raciocinar sobre eles já aparecem neste capítulo.

Não é necessário enviar respostas para revisão nem registrá-las aqui. Volte a esta seção apenas quando quiser verificar se consegue explicar o assunto sem consultar o texto.
## O que levar deste capítulo

- Um projeto Python deve declarar suas dependências e não depender do estado global da máquina.
- `.venv` isola a instalação local; `pyproject.toml` declara a intenção; `uv.lock` registra a resolução reproduzível.
- `uv run` é a maneira segura de executar ferramentas no contexto do projeto.
- Primeiro criamos um ciclo de verificação confiável; depois aumentamos a complexidade.

## Checklist

- [ ] `uv --version` funciona.
- [ ] O PyTool possui `pyproject.toml`, `uv.lock` e `.venv` local.
- [ ] `uv sync` termina sem erro.
- [ ] Ruff passa em modo check e format check.
- [ ] pytest retorna `1 passed`.
 [ ] Reservei um momento para refletir ou praticar os exercícios.

## Leitura complementar

- [PEP 20 — The Zen of Python](https://peps.python.org/pep-0020/)
- [PEP 621 — Project metadata](https://peps.python.org/pep-0621/)
- [Documentação do uv](https://docs.astral.sh/uv/)

## Ficha do capítulo

- **Capítulo:** 1
- **Dificuldade:** ⭐☆☆☆☆
- **Duração estimada:** 45–60 minutos
- **Etapa do PyTool:** Fundação do PyTool
- **Pré-requisitos:** Python e VS Code instalados
- **Estado:** em andamento
