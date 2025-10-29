# ==========================================
# 🧩 DevKickStart — Python Módulo 1
# Exemplos práticos organizados por tema
# ==========================================
#
# Conteúdo:
#
# 1. Variáveis e tipos
# 2. Condicionais
# 3. Repetições (loops)
# 4. Funções
# 5. Listas e dicionários
# 6. Mini projeto — Sistema de Cadastro
# 7. Desafios do módulo
#
#  ==========================================


# ==========================================
# 1️⃣ VARIÁVEIS E TIPOS DE DADOS
# ==========================================

print("\n=== VARIÁVEIS E TIPOS DE DADOS ===")

# Texto (string)
nome = "Nikollas"
print("Nome:", nome, "| tipo:", type(nome))

# Número inteiro (int)
idade = 21
print("Idade:", idade, "| tipo:", type(idade))

# Número decimal (float)
altura = 1.78
print("Altura:", altura, "| tipo:", type(altura))

# Booleano (bool)
ativo = True
print("Ativo:", ativo, "| tipo:", type(ativo))

# Conversões de tipo
nota_texto = "8.5"
nota_numero = float(nota_texto)
print("Nota (float):", nota_numero)

# f-strings
print(f"{nome} tem {idade} anos e {altura}m de altura. Ativo? {ativo}")


# ==========================================
# 2️⃣ CONDICIONAIS
# ==========================================

print("\n=== CONDICIONAIS ===")

idade = 17
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")

categoria = "estudante"
if categoria == "estudante":
    desconto = 0.5
elif categoria == "professor":
    desconto = 0.3
else:
    desconto = 0.0
print(f"Desconto aplicado: {desconto * 100:.0f}%")

nota = 7.2
situacao = "Aprovado" if nota >= 6 else "Reprovado"
print("Situação:", situacao)


# ==========================================
# 3️⃣ REPETIÇÕES (LOOPS)
# ==========================================

print("\n=== REPETIÇÕES (LOOPS) ===")

for i in range(5):
    print("Contagem:", i)

frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print("Fruta:", fruta)

senha_correta = "1234"
tentativas = 0
senha = ""

while senha != senha_correta and tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

print("Acesso permitido!" if senha == senha_correta else "Bloqueado. Muitas tentativas.")


# ==========================================
# 4️⃣ FUNÇÕES
# ==========================================

print("\n=== FUNÇÕES ===")

def saudacao(nome: str) -> None:
    print(f"Olá, {nome}! Bem-vindo(a) ao DevKickStart.")

def soma(a: float, b: float) -> float:
    return a + b

def eh_par(n: int) -> bool:
    return n % 2 == 0

saudacao("Nikollas")
print("Soma(3, 7) =", soma(3, 7))
print("É par?", eh_par(10))


# ==========================================
# 5️⃣ LISTAS E DICIONÁRIOS
# ==========================================

print("\n=== LISTAS E DICIONÁRIOS ===")

frutas = ["maçã", "banana", "laranja"]
frutas.append("morango")
frutas.insert(1, "pera")
removida = frutas.pop()
print("Frutas:", frutas, "| Removida:", removida)
print("Primeira fruta:", frutas[0])
print("Do índice 1 ao 2:", frutas[1:3])

pessoa = {"nome": "Ana", "idade": 25, "cidade": "Goiânia"}
pessoa["profissao"] = "Dev"
print("Pessoa:", pessoa)
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# ==========================================
# 6️⃣ MINI PROJETO — SISTEMA DE CADASTRO
# ==========================================

print("\n=== MINI PROJETO: CADASTRO DE USUÁRIOS ===")

import os
from typing import List, Dict

usuarios: List[Dict[str, str]] = []

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")

def mostrar_menu():
    print("=== MENU ===")
    print("1. Cadastrar novo usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário por nome")
    print("4. Sair")

def cadastrar_usuario():
    limpar_tela()
    print("--- Cadastro de Usuário ---")
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()
    email = input("Email: ").strip()

    if not nome or not idade or not email:
        print("⚠️ Todos os campos são obrigatórios.")
        return pausar()

    usuarios.append({"nome": nome, "idade": idade, "email": email})
    print(f"✅ Usuário '{nome}' cadastrado com sucesso!")
    pausar()

def listar_usuarios():
    limpar_tela()
    print("--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, u in enumerate(usuarios, start=1):
            print(f"{i}. {u['nome']} ({u['idade']} anos) - {u['email']}")
    pausar()

def buscar_usuario():
    limpar_tela()
    print("--- Buscar Usuário ---")
    termo = input("Digite o nome a buscar: ").strip().lower()
    encontrados = [u for u in usuarios if termo in u["nome"].lower()]
    if encontrados:
        print(f"\n{len(encontrados)} usuário(s) encontrado(s):")
        for u in encontrados:
            print(f"- {u['nome']} ({u['idade']} anos) - {u['email']}")
    else:
        print("🔍 Nenhum usuário encontrado.")
    pausar()

def iniciar_sistema():
    while True:
        limpar_tela()
        mostrar_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()
        if opcao == "1": cadastrar_usuario()
        elif opcao == "2": listar_usuarios()
        elif opcao == "3": buscar_usuario()
        elif opcao == "4":
            print("Encerrando... 👋")
            break
        else:
            print("Opção inválida!")
            pausar()

# Descomente para rodar:
# if __name__ == "__main__":
#     iniciar_sistema()


# ==========================================
# 7️⃣ DESAFIOS DO MÓDULO
# ==========================================

print("\n=== DESAFIOS DO MÓDULO ===")

# 1. Média de 3 notas
def media_tres_notas():
    notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]
    media = sum(notas) / 3
    print(f"Média final: {media:.2f}")

# 2. Sistema de login simples
def sistema_login():
    usuario, senha = "admin", "1234"
    login = input("Usuário: ")
    password = input("Senha: ")
    if login == usuario and password == senha:
        print("✅ Login bem-sucedido!")
    else:
        print("❌ Usuário ou senha incorretos.")

# 3. Par ou ímpar
def par_ou_impar():
    n = int(input("Digite um número: "))
    print("É par!" if n % 2 == 0 else "É ímpar!")

# 4. Dicionário de aluno
def aluno_dados():
    aluno = {
        "nome": input("Nome: "),
        "curso": input("Curso: "),
        "idade": int(input("Idade: "))
    }
    print("📘 Dados do aluno:", aluno)

# 5. Calculadora simples
def calculadora():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    op = input("Operação (+, -, *, /): ")

    if op == "+": print("Resultado:", a + b)
    elif op == "-": print("Resultado:", a - b)
    elif op == "*": print("Resultado:", a * b)
    elif op == "/": print("Resultado:", a / b if b != 0 else "Erro: divisão por zero!")
    else: print("Operação inválida.")

# Descomente o que quiser testar:
# media_tres_notas()
# sistema_login()
# par_ou_impar()
# aluno_dados()
# calculadora()
