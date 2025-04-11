

# Apostila: Curso Introdutório de Python

> Esta apostila faz parte do projeto **DevKickStart** e tem como objetivo ensinar os conceitos básicos da linguagem Python para iniciantes. Aqui você encontrará teoria detalhada, exemplos comentados, práticas e exercícios que te ajudarão a iniciar sua jornada na programação.

---

## Índice

1. [Introdução ao Python](#1-introdução-ao-python)
2. [Instalação e configuração do ambiente](#2-instalação-e-configuração-do-ambiente)
3. [Primeiros passos com Python](#3-primeiros-passos-com-python)
4. [Tipos de dados](#4-tiposs-de-dados)
5. [Variáveis e operações](#5-variáveis-e-operações)
6. [Estruturas condicionais](#6-estruturas-condicionais)
7. [Estruturas de repetição](#7-estruturas-de-repetição)
8. [Funções](#8-funções)
9. [Listas e dicionários](#9-listas-e-dicionários)
10. [Boas práticas e dicas](#10-boas-práticas-e-dicas)
11. [Exercícios propostos](#11-exercícios-propostos)
12. [Fontes recomendadas](#12-fontes-recomendadas)

---

## 1. Introdução ao Python

Python é uma linguagem de **alto nível**, criada por **Guido van Rossum** e lançada em 1991. Ela se destaca por sua **legibilidade**, **simples sintaxe** e **potente funcionalidade**, sendo usada amplamente em várias áreas:

- **Desenvolvimento Web**: frameworks como Django e Flask.
- **Ciência de Dados**: bibliotecas como Pandas, Numpy, Matplotlib e SciPy.
- **Inteligência Artificial e Machine Learning**: bibliotecas como TensorFlow, PyTorch, Scikit-learn.
- **Automação**: Python é amplamente usado para automação de tarefas e scripts.

A simplicidade do Python faz dele uma excelente linguagem de **iniciação** para novos programadores.

---

## 2. Instalação e configuração do ambiente

### Instalação:

1. Acesse <a href="https://www.python.org/downloads/" target="_blank">Python.org</a> e baixe a versão apropriada.
2. Durante a instalação, marque a opção **"Add Python to PATH"** para configurar automaticamente o ambiente.

### Verificação:

Abra o terminal e digite:
```bash
python --version
```
Se retornar a versão do Python instalada, a configuração foi bem-sucedida.

### IDEs recomendadas:

- **VS Code**: Editor de código leve, com suporte a Python através de extensões.
- **PyCharm**: IDE robusta focada em Python.
- **Thonny**: IDE simples para iniciantes.
- **Jupyter Notebook**: Recomendado para cientistas de dados, para criar e compartilhar documentos que contenham código Python.

---

## 3. Primeiros passos com Python

### Seu primeiro programa:

```python
# Exibindo uma mensagem no console
print("Olá, mundo!")
```

Explicação: O comando `print()` exibe o texto entre parênteses na tela. Este é o primeiro passo para interagir com o programa e é comumente o primeiro código executado por iniciantes.

### Comentários:

Comentários são ignorados pelo Python e servem para descrever o que o código faz, tornando o código mais legível.

```python
# Isso é um comentário
```

---

## 4. Tipos de dados

Python é uma linguagem **tipada dinamicamente**, o que significa que as variáveis não precisam declarar seu tipo explicitamente. Aqui estão os tipos básicos:

- **int**: Números inteiros.
- **float**: Números decimais (ponto flutuante).
- **str**: Strings, ou seja, sequências de caracteres.
- **bool**: Valores booleanos `True` ou `False`.
- **list**: Listas, que armazenam múltiplos valores em uma sequência ordenada.
- **dict**: Dicionários, que armazenam pares chave-valor.

Exemplo de uso:

```python
# Inteiro
numero = 10

# Float
pi = 3.14

# String
nome = "João"

# Booleano
verdadeiro = True

# Lista
lista = [1, 2, 3]

# Dicionário
pessoa = {"nome": "Ana", "idade": 25}
```

Conversão de tipos:

```python
# Convertendo string para inteiro
numero = int("10")

# Convertendo para float
decimal = float("3.14")

# Convertendo número para string
texto = str(25)
```

---

## 5. Variáveis e operações

### Variáveis:

Variáveis são usadas para armazenar dados na memória. Você pode criar uma variável e armazenar um valor nela:

```python
nome = "João"  # String
idade = 20     # Inteiro
```

### Operadores:

Python tem diversos operadores, que podem ser divididos em três grupos principais:

1. **Aritméticos**: Usados para operações matemáticas.
   - `+`, `-`, `*`, `/`, `**`, `//`, `%`

   Exemplo:
   ```python
   a = 5
   b = 3
   soma = a + b  # resultado 8
   ```

2. **Relacionais**: Usados para comparações entre dois valores.
   - `==`, `!=`, `>`, `<`, `>=`, `<=`

   Exemplo:
   ```python
   a = 5
   b = 3
   resultado = a > b  # True
   ```

3. **Lógicos**: Usados para combinar expressões booleanas.
   - `and`, `or`, `not`

   Exemplo:
   ```python
   a = True
   b = False
   resultado = a and b  # False
   ```

---

## 6. Estruturas condicionais

As estruturas condicionais permitem executar diferentes blocos de código dependendo de condições.

### If, Elif, Else:

```python
idade = 18

# Verificando a maioridade
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")
```

Explicação: O bloco de código dentro de `if` é executado quando a condição é verdadeira, o `elif` é para condições alternativas e o `else` é executado quando todas as condições anteriores são falsas.

---

## 7. Estruturas de repetição

### For:

Usado quando você sabe quantas vezes deseja repetir uma ação.

```python
# Iterando de 0 a 4
for i in range(5):
    print(i)
```

### While:

Usado quando você deseja repetir um bloco de código enquanto uma condição for verdadeira.

```python
# Loop até a senha ser correta
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
```

---

## 8. Funções

Funções permitem organizar o código em blocos reutilizáveis.

### Função simples:

```python
# Função sem parâmetros
def saudacao():
    print("Bem-vindo!")
```

### Função com parâmetros e retorno:

```python
# Função que soma dois números
def soma(a, b):
    return a + b

print(soma(3, 4))  # 7
```

---

## 9. Listas e dicionários

### Lista:

Uma lista armazena múltiplos itens ordenados.

```python
frutas = ["maçã", "banana", "laranja"]
frutas.append("morango")  # Adicionando item à lista
```

### Dicionário:

Dicionários armazenam dados no formato chave-valor.

```python
pessoa = {"nome": "Ana", "idade": 25}
print(pessoa["nome"])  # Acessando a chave "nome"
```

---

## 10. Boas práticas e dicas

- **Nomeie variáveis** de forma clara e descritiva.
- Use **comentários** para explicar o propósito de blocos de código, especialmente se forem complexos.
- **Evite repetição de código**: sempre que possível, crie funções.
- Teste seu código com **diferentes entradas** para garantir que funcione corretamente.

---

## 11. Exercícios propostos

1. Escreva um programa que calcule a média de 3 notas.
2. Crie uma função que verifique se um número é par ou ímpar.
3. Simule um sistema de login com senha.
4. Crie um dicionário com dados pessoais (nome, idade, endereço) e mostre-os.
5. Faça um programa que simula uma calculadora de soma e subtração.

---

## 12. Fontes recomendadas

- [Documentação oficial (PT-BR)](https://docs.python.org/pt-br/3/)
- [Curso em Vídeo - Python](https://youtube.com/playlist?list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0)
- [Python para Iniciantes - Microsoft](https://learn.microsoft.com/pt-br/shows/intro-to-python-development/)
- [W3Schools - Python](https://www.w3schools.com/python/)
- [Exercism - Python](https://exercism.io/tracks/python)

---

### Créditos

- Apostila desenvolvida por [@imnikollasdev](https://github.com/imnikollasdev)
- Projeto: **DevKickStart**

---

> *Fim da apostila de Python - Módulo introdutório*        
