"""
Sistema simples de cadastro de usuários
Autor: Níkollas Grégory @imnikollasdev
Data: 2025-04-09
Descrição: Este script simula um pequeno sistema de cadastro com menu, usando conceitos básicos de Python.
"""

usuarios = []  # Lista para armazenar os usuários


def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Cadastrar novo usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário por nome")
    print("4. Sair")


def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()
    email = input("Email: ").strip()

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print(f"✅ Usuário '{nome}' cadastrado com sucesso!")


def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario['nome']} ({usuario['idade']} anos) - {usuario['email']}")


def buscar_usuario():
    print("\n--- Buscar Usuário ---")
    termo = input("Digite o nome a buscar: ").strip().lower()
    encontrados = [u for u in usuarios if termo in u['nome'].lower()]

    if encontrados:
        print(f"\n{len(encontrados)} usuário(s) encontrado(s):")
        for usuario in encontrados:
            print(f"- {usuario['nome']} ({usuario['idade']} anos) - {usuario['email']}")
    else:
        print("🔍 Nenhum usuário encontrado com esse nome.")


# Loop principal
def iniciar_sistema():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            buscar_usuario()
        elif opcao == '4':
            print("Encerrando o sistema... 👋")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Ponto de entrada
if __name__ == "__main__":
    iniciar_sistema()
