# 🐍 Python — Módulo 1: Fundamentos

> Esta apostila faz parte do projeto **DevKickStart** e tem como objetivo ensinar os conceitos básicos da linguagem **Python** para iniciantes.  
> Aqui você encontrará teoria explicada de forma simples, exemplos comentados, boas práticas e exercícios para desenvolver suas habilidades desde o zero.

---

<p align="center">
  <a href="./python.md">🏠 Voltar à Trilha Python</a> |
  <a href="./modulo2_intermediario.md">➡️ Próximo Módulo</a>
</p>

---

## 🧭 Introdução

Seja bem-vindo à sua jornada com **Python**!  
Esta linguagem é famosa por ser **fácil de aprender**, mas poderosa o bastante para estar presente em áreas como **inteligência artificial**, **automação**, **web**, e **ciência de dados**.

Pense no Python como uma “língua universal da tecnologia” — simples, direta e expressiva.  
Você não precisa decorar regras complicadas para começar a criar algo funcional.

---

## 1️⃣ O que é Python?

Python é uma linguagem de **alto nível**, criada em 1991 por **Guido van Rossum**.  
O objetivo era simples: criar uma linguagem que fosse **tão legível quanto o inglês**.

Ela é usada por empresas como Google, Netflix, NASA e Instagram.  
Por quê? Porque é **versátil**, **rápida de desenvolver** e **fácil de manter**.

> 💡 **Curiosidade:** O nome “Python” não vem do animal, e sim do grupo de comédia britânico “Monty Python”.  
> É por isso que muitos exemplos na documentação oficial são meio engraçados!

---

## 2️⃣ Instalando o Python e o Ambiente

### 🧩 Passo 1 — Instalação

Acesse o site oficial:  
👉 [python.org/downloads](https://www.python.org/downloads/)

Durante a instalação, **marque a opção “Add Python to PATH”** — isso faz o sistema reconhecer o comando `python` no terminal.

---

### 🧰 Passo 2 — Testando a instalação

Abra o **Prompt de Comando** (Windows) ou o **Terminal** (Linux/macOS) e digite:

```bash
python --version
```

Se aparecer algo como `Python 3.12.0`, parabéns 🎉 — você está pronto para começar!

---

### 💡 Dica de Ouro: IDEs Recomendadas

| IDE | Descrição |
|-----|------------|
| 🧠 **VS Code** | Leve, personalizável e ideal para iniciantes. |
| 🐍 **PyCharm** | Focada em Python, com ferramentas integradas. |
| 💼 **Jupyter Notebook** | Usada por cientistas de dados e estudantes. |
| 🪶 **Thonny** | Feita especialmente para quem está começando. |

---

## 3️⃣ Seu primeiro código

Abra o seu editor e digite:

```python
print("Olá, mundo!")
```

> 🗣️ *O comando `print()` é a forma de “falar” com o computador.*  
> Ele imprime uma mensagem na tela. Simples e direto!

### 🗒️ Comentários

Comentários são anotações dentro do código. Eles **não são executados**, mas ajudam a entender o que o programa faz.

```python
# Este é um comentário
print("Comentários deixam o código mais legível!")
```

> 💬 **Dica:** Use comentários para explicar o “porquê” do código, não o “como”.

---

## 4️⃣ Tipos de dados

Python é **dinamicamente tipado**, ou seja, você não precisa dizer o tipo da variável — ele descobre sozinho.

| Tipo | Exemplo | Descrição |
|------|----------|-----------|
| int | `10` | Número inteiro |
| float | `3.14` | Número decimal |
| str | `"Olá"` | Texto |
| bool | `True` / `False` | Valor lógico |
| list | `[1, 2, 3]` | Lista de valores |
| dict | `{"nome": "Ana"}` | Dicionário (chave-valor) |

Exemplo prático:

```python
nome = "Nikollas"
idade = 21
altura = 1.78
ativo = True

print(nome, idade, altura, ativo)
```

> 🧠 **Curiosidade:** tudo em Python é um **objeto**, até os números!

---

## 5️⃣ Variáveis e Operações

Uma variável é como uma **caixa que guarda um valor**.  
Você pode dar um nome a ela e usá-la depois:

```python
mensagem = "Bem-vindo!"
print(mensagem)
```

### 🧮 Operadores Matemáticos

| Operador | Exemplo | Resultado |
|-----------|----------|------------|
| `+` | `5 + 3` | `8` |
| `-` | `10 - 2` | `8` |
| `*` | `4 * 3` | `12` |
| `/` | `8 / 2` | `4.0` |
| `//` | `7 // 2` | `3` (divisão inteira) |
| `%` | `7 % 2` | `1` (resto) |
| `**` | `2 ** 3` | `8` (potência) |

Exemplo:
```python
a = 10
b = 3
print("Soma:", a + b)
print("Resto da divisão:", a % b)
```

> 💡 **Boa prática:** use nomes claros — `idade`, `saldo`, `nota_final`.  
> Evite nomes genéricos como `x` ou `data1`.

---

## 6️⃣ Estruturas Condicionais

E se quisermos **tomar decisões** no programa?

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

> ⚙️ *O Python lê o código de cima pra baixo e respeita a indentação (os espaços).*

---

## 7️⃣ Repetições (Loops)

Às vezes, queremos repetir uma ação várias vezes — é aí que entram os **loops**.

### 🔁 For
```python
for i in range(5):
    print("Contagem:", i)
```
> Executa 5 vezes, de 0 até 4.

### 🔂 While
```python
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso liberado!")
```

---

## 8️⃣ Funções

Funções organizam o código e evitam repetição.

```python
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo ao DevKickStart.")
```

> 💬 *Elas são como “mini programas” dentro do seu programa.*

---

## 9️⃣ Listas e Dicionários

Listas guardam vários valores em sequência:
```python
frutas = ["maçã", "banana", "uva"]
frutas.append("morango")
```

Dicionários armazenam dados com chaves e valores:
```python
pessoa = {"nome": "Ana", "idade": 25}
print(pessoa["nome"])
```

---

## 🔟 Boas Práticas

- 🧠 Use nomes descritivos  
- ✍️ Comente blocos importantes  
- 📦 Organize o código em funções  
- 🔁 Teste seu código com diferentes entradas

---

## 🧩 Desafios

1. Crie um programa que calcule a média de 3 notas.  
2. Faça um sistema de login com senha.  
3. Escreva uma função que verifique se um número é par ou ímpar.  
4. Monte um dicionário com dados de um aluno (nome, curso, idade).  
5. Faça uma calculadora simples (soma, subtração, multiplicação e divisão).

---

## 📚 Fontes recomendadas

- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)
- [W3Schools - Python](https://www.w3schools.com/python/)
- [Python Brasil](https://wiki.python.org.br/)

---

<p align="center">
  <a href="./python.md">🏠 Voltar à Trilha Python</a> |
  <a href="./modulo2_intermediario.md">➡️ Ir para o Módulo 2</a>
</p>
