# 🐍 Python — Módulo 3: Avançado

> Esta apostila faz parte do projeto **DevKickStart** e tem como objetivo levar seu **Python** para o nível avançado.  
> Você aprenderá conceitos sólidos de **Programação Orientada a Objetos (POO)**, **exceções personalizadas**, **módulos e pacotes**, **tipagem estática**, **requisições HTTP**, e **testes automatizados** — sempre com explicações claras e exemplos práticos.

---

<p align="center">
  <a href="./modulo2_intermediario.md">⬅️ Voltar ao Módulo 2</a> |
  <a href="./python.md">🏠 Voltar à Trilha Python</a>
</p>

---

## 📘 Índice

- [🐍 Python — Módulo 3: Avançado](#-python--módulo-3-avançado)
  - [📘 Índice](#-índice)
  - [1. Revisão: O que é POO?](#1-revisão-o-que-é-poo)
  - [2. Classes e Objetos Avançados](#2-classes-e-objetos-avançados)
  - [3. Encapsulamento e Propriedades](#3-encapsulamento-e-propriedades)
    - [🔸 Propriedades (`@property`)](#-propriedades-property)
  - [4. Herança e Polimorfismo](#4-herança-e-polimorfismo)
  - [5. Exceções Personalizadas](#5-exceções-personalizadas)
  - [6. Módulos e Pacotes](#6-módulos-e-pacotes)
    - [Exemplo:](#exemplo)
  - [7. Tipagem Estática (Type Hints)](#7-tipagem-estática-type-hints)
  - [8. Consumo de APIs com `requests`](#8-consumo-de-apis-com-requests)
  - [9. Testes Automatizados com `pytest`](#9-testes-automatizados-com-pytest)
  - [10. Mini Projeto: Gerenciador de Tarefas](#10-mini-projeto-gerenciador-de-tarefas)
  - [11. Boas Práticas e Dicas Finais](#11-boas-práticas-e-dicas-finais)
  - [12. Fontes Recomendadas](#12-fontes-recomendadas)
    - [✍️ Créditos](#️-créditos)

---

## 1. Revisão: O que é POO?

A **Programação Orientada a Objetos (POO)** é um paradigma que organiza o código em **classes** (modelos) e **objetos** (instâncias).  
Ela facilita o reuso de código e a manutenção de sistemas grandes.

Os quatro pilares principais da POO são:

| Pilar | Descrição |
|-------|------------|
| **Encapsulamento** | Esconder detalhes internos de uma classe. |
| **Herança** | Reutilizar e estender o comportamento de outras classes. |
| **Polimorfismo** | Permitir diferentes comportamentos para o mesmo método. |
| **Abstração** | Focar apenas no que é essencial. |

---

## 2. Classes e Objetos Avançados

Agora que você já entende o básico de classes, vamos aprimorar a estrutura.

```python
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> None:
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")

    def aniversario(self) -> None:
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")

p1 = Pessoa("Níkollas", 21)
p1.apresentar()
p1.aniversario()
```

> 💡 Note que o uso de **type hints** (`: str`, `-> None`) ajuda na legibilidade e manutenção.

---

## 3. Encapsulamento e Propriedades

Encapsular significa **proteger os atributos** de acesso direto.  
Usamos `__` (dois underlines) para torná-los privados.

```python
class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor

    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

conta = ContaBancaria("Níkollas", 1000)
conta.depositar(200)
conta.ver_saldo()
```

### 🔸 Propriedades (`@property`)

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self._preco = valor
        else:
            print("Preço inválido!")
```

---

## 4. Herança e Polimorfismo

A herança permite criar novas classes baseadas em outras.

```python
class Animal:
    def falar(self):
        print("Som genérico...")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

animais = [Cachorro(), Gato()]
for a in animais:
    a.falar()  # Polimorfismo em ação
```

> 💬 *O mesmo método “falar()” se comporta de maneiras diferentes conforme o objeto.*

---

## 5. Exceções Personalizadas

Você pode criar **suas próprias exceções** para tratar erros específicos.

```python
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f"Saldo insuficiente: {saldo} < {valor}")
```

Uso prático:

```python
try:
    saldo = 100
    saque = 200
    if saque > saldo:
        raise SaldoInsuficienteError(saldo, saque)
except SaldoInsuficienteError as e:
    print("Erro:", e)
```

---

## 6. Módulos e Pacotes

Em Python, um **módulo** é simplesmente um arquivo `.py`.  
Um **pacote** é uma pasta com vários módulos e um arquivo `__init__.py`.

### Exemplo:

```
meu_projeto/
├── main.py
└── utilidades/
    ├── __init__.py
    └── calculadora.py
```

```python
# calculadora.py
def somar(a, b):
    return a + b

# main.py
from utilidades.calculadora import somar
print(somar(2, 3))
```

---

## 7. Tipagem Estática (Type Hints)

Python é dinâmico, mas podemos **declarar tipos** para melhorar a clareza.

```python
def dividir(a: float, b: float) -> float:
    return a / b
```

> 💡 Ferramentas como `mypy` verificam erros de tipo antes da execução:
> ```bash
> mypy arquivo.py
> ```

---

## 8. Consumo de APIs com `requests`

Podemos conectar nosso código a **serviços externos** via HTTP.

```python
import requests

resposta = requests.get("https://api.github.com/users/imnikollasdev")
if resposta.status_code == 200:
    dados = resposta.json()
    print(f"Usuário: {dados['login']} - Repositórios: {dados['public_repos']}")
else:
    print("Falha na requisição:", resposta.status_code)
```

> 🌐 *Essa técnica é usada em aplicações que consomem dados da web (como dashboards ou bots).*

---

## 9. Testes Automatizados com `pytest`

Testes automatizados garantem que o código continue funcionando ao longo do tempo.

```python
# arquivo: calculadora.py
def soma(a, b):
    return a + b
```

```python
# arquivo: test_calculadora.py
from calculadora import soma

def test_soma():
    assert soma(2, 3) == 5
```

Execução:

```bash
pytest test_calculadora.py
```

---

## 10. Mini Projeto: Gerenciador de Tarefas

Desenvolva um pequeno sistema que:
- Crie, liste e conclua tarefas.
- Armazene os dados em um arquivo `tarefas.json`.
- Use classes (`Tarefa`, `GerenciadorTarefas`) para organizar a lógica.
- Aplique tratamento de erros e boas práticas de POO.

---

## 11. Boas Práticas e Dicas Finais

- Sempre documente o código com *docstrings* (`"""texto"""` dentro das funções).  
- Use exceções personalizadas para erros esperados.  
- Escreva testes simples para funções críticas.  
- Use `virtualenv` ou `venv` para isolar dependências.  
- Aplique o princípio **KISS**: *Keep It Simple, Stupid!*  

---

## 12. Fontes Recomendadas

- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)
- [Real Python — Advanced Topics](https://realpython.com/)
- [PEP 8 — Guia de estilo oficial do Python](https://peps.python.org/pep-0008/)
- [Requests Library Docs](https://requests.readthedocs.io/en/latest/)
- [Pytest Documentation](https://docs.pytest.org/en/latest/)

---

### ✍️ Créditos

Apostila desenvolvida por [@imnikollasdev](https://github.com/imnikollasdev)  
Projeto: **DevKickStart**

---

<p align="center">
  <a href="./modulo2_intermediario.md">⬅️ Voltar ao Módulo 2</a> |
  <a href="./python.md">🏠 Voltar à Trilha Python</a>
</p>
