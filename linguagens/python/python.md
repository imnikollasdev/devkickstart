# Apostila: Curso Introdutório de Python

> Esta apostila faz parte do projeto **DevKickstart** e tem como objetivo ensinar os conceitos básicos da linguagem Python para iniciantes. Aqui você encontrará teoria, exemplos, práticas e exercícios que te ajudarão a iniciar sua jornada na programação.

---

## Índice

1. Introdução ao Python
2. Instalação e configuração do ambiente
3. Primeiros passos com Python
4. Tipos de dados
5. Variáveis e operações
6. Estruturas condicionais
7. Estruturas de repetição
8. Funções
9. Listas e dicionários
10. Boas práticas e dicas
11. Exercícios propostos
12. Fontes recomendadas

---

## 1. Introdução ao Python

Python é uma linguagem de programação de alto nível, criada por Guido van Rossum e lançada em 1991. Ela é reconhecida por sua legibilidade e simplicidade. É amplamente usada em diversas áreas como:

- Desenvolvimento web
- Ciência de dados
- Inteligência Artificial
- Automação de tarefas
- Criação de scripts

Python é multiplataforma, gratuito e tem uma comunidade muito ativa.

---

## 2. Instalação e configuração do ambiente

### Instalação:

- Acesse: https://www.python.org/downloads/
- Baixe a versão compatível com seu sistema operacional
- Marque a opção "Add Python to PATH" durante a instalação

### Verificação:
Abra o terminal e digite:
```bash
python --version
```

### IDEs recomendadas:
- VS Code
- PyCharm
- Thonny
- Jupyter Notebook (para cientistas de dados)

---

## 3. Primeiros passos com Python

### Seu primeiro programa:
```python
print("Olá, mundo!")
```

### Comentários:
```python
# Isso é um comentário
```

---

## 4. Tipos de dados

| Tipo  | Exemplo              |
|-------|----------------------|
| int   | 10                   |
| float | 3.14                 |
| str   | "texto"              |
| bool  | True, False          |
| list  | [1, 2, 3]            |
| dict  | {"nome": "Ana"}      |

Conversão de tipos:
```python
int("10")
float("3.14")
str(25)
```

---

## 5. Variáveis e operações

### Variáveis:
```python
nome = "João"
idade = 20
```

### Operadores:
- Aritméticos: `+`, `-`, `*`, `/`, `**`, `//`, `%`
- Relacionais: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Lógicos: `and`, `or`, `not`

---

## 6. Estruturas condicionais

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")
```

---

## 7. Estruturas de repetição

### For:
```python
for i in range(5):
    print(i)
```

### While:
```python
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
```

---

## 8. Funções

### Função simples:
```python
def saudacao():
    print("Bem-vindo!")
```

### Função com parâmetros e retorno:
```python
def soma(a, b):
    return a + b

print(soma(3, 4))
```

---

## 9. Listas e dicionários

### Lista:
```python
frutas = ["maçã", "banana"]
frutas.append("laranja")
```

### Dicionário:
```python
pessoa = {"nome": "Ana", "idade": 25}
print(pessoa["nome"])
```

---

## 10. Boas práticas e dicas

- Nomeie variáveis de forma clara
- Comente apenas o necessário
- Evite códigos duplicados
- Teste seus programas com diferentes entradas

---

## 11. Exercícios propostos

1. Escreva um programa que calcule a média de 3 notas
2. Crie uma função que verifique se um número é par
3. Simule um sistema de login com senha
4. Crie um dicionário com dados pessoais e mostre-os
5. Faça um programa que simula uma calculadora

---

## 12. Fontes recomendadas
- [Documentação oficial (PT-BR)](https://docs.python.org/pt-br/3/)
- [Curso em Vídeo - Python](https://youtube.com/playlist?list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&si=JLyPRTLwmdIgAh44)
- [Python para Iniciantes](https://learn.microsoft.com/pt-br/shows/intro-to-python-development/)
- [W3Schools - Python](https://www.w3schools.com/python/)
- [Exercism - Python](https://exercism.io/tracks/python)

---

> *Fim da apostila de Python - Módulo introdutório*        
