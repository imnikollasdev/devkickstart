# 🐍 Python — Módulo 2: Intermediário

> Esta apostila faz parte do projeto **DevKickStart** e tem como objetivo aprofundar seus conhecimentos em **Python**, indo além do básico.  
> Aqui você aprenderá estruturas de dados mais poderosas, manipulação de arquivos, funções modernas, tratamento de erros e conceitos iniciais de Programação Orientada a Objetos (POO).  
> Cada seção é acompanhada de exemplos explicados e exercícios para fixar o conteúdo.

---

<p align="center">
  <a href="./modulo1_fundamentos.md">⬅️ Voltar ao Módulo 1</a> |
  <a href="./python.md">🏠 Voltar à Trilha Python</a> |
  <a href="./modulo3_avancado.md">➡️ Próximo Módulo</a>
</p>

---

## 📘 Índice

- [🐍 Python — Módulo 2: Intermediário](#-python--módulo-2-intermediário)
  - [📘 Índice](#-índice)
  - [1. Listas e Tuplas Avançadas](#1-listas-e-tuplas-avançadas)
    - [🔹 Listas aninhadas](#-listas-aninhadas)
    - [🔸 Fatiamento (slicing)](#-fatiamento-slicing)
    - [🔸 Tuplas](#-tuplas)
  - [2. Dicionários e Conjuntos (Sets)](#2-dicionários-e-conjuntos-sets)
    - [📘 Dicionários](#-dicionários)
    - [🔹 Conjuntos (Sets)](#-conjuntos-sets)
  - [3. Funções com Parâmetros Avançados](#3-funções-com-parâmetros-avançados)
    - [🔸 Argumentos variáveis](#-argumentos-variáveis)
    - [🔸 Argumentos nomeados (`**kwargs`)](#-argumentos-nomeados-kwargs)
  - [4. Expressões Lambda e Funções Anônimas](#4-expressões-lambda-e-funções-anônimas)
  - [5. Manipulação de Arquivos](#5-manipulação-de-arquivos)
    - [✍️ Escrevendo em um arquivo](#️-escrevendo-em-um-arquivo)
    - [📖 Lendo um arquivo](#-lendo-um-arquivo)
    - [🧩 Modo append](#-modo-append)
  - [6. Tratamento de Erros e Exceções](#6-tratamento-de-erros-e-exceções)
  - [7. Introdução à POO](#7-introdução-à-poo)
  - [8. Boas Práticas e Dicas](#8-boas-práticas-e-dicas)
  - [9. Exercícios Propostos](#9-exercícios-propostos)
  - [10. Fontes Recomendadas](#10-fontes-recomendadas)
    - [✍️ Créditos](#️-créditos)

---

## 1. Listas e Tuplas Avançadas

No módulo anterior você aprendeu a criar listas simples.  
Agora vamos explorar recursos mais poderosos — **listas aninhadas**, **fatiamento** e **tuplas**.

### 🔹 Listas aninhadas

Uma lista pode conter outras listas.  
Isso é útil, por exemplo, para representar tabelas, grades ou matrizes:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])  # Exibe 6
```

> 💡 *Dica:* use loops `for` duplos para percorrer listas aninhadas.

### 🔸 Fatiamento (slicing)

Podemos acessar partes específicas de uma lista:

```python
frutas = ["maçã", "banana", "laranja", "morango", "uva"]
print(frutas[1:4])   # ['banana', 'laranja', 'morango']
print(frutas[-2:])   # ['morango', 'uva']
```

### 🔸 Tuplas

Tuplas são como listas, mas **imutáveis**.  
Ou seja, depois de criadas, não podem ser alteradas:

```python
cores = ("vermelho", "azul", "verde")
print(cores[0])
# cores[1] = "amarelo"  # ❌ erro: não é possível alterar
```

> Use tuplas para representar dados fixos (ex: coordenadas, configurações).

---

## 2. Dicionários e Conjuntos (Sets)

### 📘 Dicionários

Dicionários armazenam pares **chave: valor**, ideais para representar objetos do mundo real:

```python
pessoa = {
    "nome": "Níkollas",
    "idade": 21,
    "cidade": "Goiânia"
}

print(pessoa["nome"])  # Níkollas
pessoa["profissao"] = "Desenvolvedor"
```

> 🧠 *Dica:* use dicionários quando precisar armazenar e acessar dados por **nomes**, não por índices.

### 🔹 Conjuntos (Sets)

Sets são coleções **sem ordem** e **sem elementos duplicados**:

```python
frutas = {"maçã", "banana", "maçã", "laranja"}
print(frutas)  # {'banana', 'maçã', 'laranja'}
```

Podem ser usados para eliminar duplicatas ou fazer operações matemáticas:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # União → {1,2,3,4,5}
print(a & b)  # Interseção → {3}
```

---

## 3. Funções com Parâmetros Avançados

### 🔸 Argumentos variáveis

Com `*args`, você pode receber **vários valores** em uma função:

```python
def somar(*numeros):
    total = sum(numeros)
    print(f"Soma total: {total}")

somar(1, 2, 3, 4, 5)
```

### 🔸 Argumentos nomeados (`**kwargs`)

Permitem receber valores com **nomes**:

```python
def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Ana", idade=25, cidade="Goiânia")
```

---

## 4. Expressões Lambda e Funções Anônimas

As **funções lambda** são funções curtas e sem nome — úteis em casos simples:

```python
quadrado = lambda x: x ** 2
print(quadrado(5))  # 25
```

Elas combinam muito bem com funções como `map`, `filter` e `reduce`.

```python
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(dobrados)  # [2,4,6,8,10]
print(pares)     # [2,4]
```

---

## 5. Manipulação de Arquivos

Agora que você domina as estruturas básicas, é hora de **salvar e ler dados externos**.  
Python facilita o trabalho com arquivos de texto.

### ✍️ Escrevendo em um arquivo

```python
with open("dados.txt", "w") as arquivo:
    arquivo.write("Bem-vindo ao DevKickStart!\n")
```

### 📖 Lendo um arquivo

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

### 🧩 Modo append

Para adicionar novas linhas sem sobrescrever o arquivo:

```python
with open("dados.txt", "a") as arquivo:
    arquivo.write("Nova linha adicionada.\n")
```

---

## 6. Tratamento de Erros e Exceções

Erros acontecem — mas você pode controlá-los.  
Use `try`, `except`, `else` e `finally` para tratar exceções.

```python
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)
except ZeroDivisionError:
    print("Erro: divisão por zero.")
except ValueError:
    print("Erro: entrada inválida.")
else:
    print("Tudo ocorreu bem!")
finally:
    print("Encerrando programa.")
```

> 💡 *Boas práticas:*  
> - Sempre trate exceções específicas.  
> - Evite capturar erros genéricos com `except:` sem tipo.  

---

## 7. Introdução à POO

A **Programação Orientada a Objetos** (POO) ajuda a organizar o código de forma mais clara e modular.  
Com ela, criamos **classes** que geram **objetos**, que possuem **atributos** (dados) e **métodos** (funções).

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Níkollas", 21)
p1.falar()
```

> 🧠 *Entenda:* `__init__` é o **construtor** da classe — ele roda automaticamente ao criar o objeto.

---

## 8. Boas Práticas e Dicas

- Use nomes de variáveis **autoexplicativos**.  
- Mantenha funções **curtas e específicas**.  
- Trate exceções sempre que o código puder falhar.  
- Evite duplicar lógica — **crie funções reutilizáveis**.  
- Documente o código com comentários claros.

---

## 9. Exercícios Propostos

1. Crie uma função que receba uma lista de números e retorne apenas os pares.  
2. Escreva um programa que salve nomes digitados pelo usuário em um arquivo `.txt`.  
3. Faça um sistema simples de cadastro de pessoas usando **classes** (`Pessoa` com nome e idade).  
4. Implemente uma função que conte quantas vogais existem em uma frase.  
5. Simule um pequeno menu com opções de leitura e escrita em arquivo.

---

## 10. Fontes Recomendadas

- [Python Intermediário - Hashtag Programação](https://www.hashtagtreinamentos.com/python-intermediario)
- [Documentação oficial - Python Classes](https://docs.python.org/pt-br/3/tutorial/classes.html)

---

### ✍️ Créditos

Apostila desenvolvida por [@imnikollasdev](https://github.com/imnikollasdev)  
Projeto: **DevKickStart**

---

<p align="center">
  <a href="./modulo1_fundamentos.md">⬅️ Voltar ao Módulo 1</a> |
  <a href="./python.md">🏠 Voltar à Trilha Python</a> |
  <a href="./modulo3_avancado.md">➡️ Próximo Módulo</a>
</p>
