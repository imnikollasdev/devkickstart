# ==========================================
# 🧩 DevKickStart — Python Módulo 2
# Exemplos práticos organizados por tema
#
# ==========================================
#
# Conteúdo:
# 1. Manipulação de arquivos (leitura/escrita)
# 2. Tratamento de erros (try/except)
# 3. Funções avançadas e lambda
# 4. Programação Orientada a Objetos (POO básica)
# 5. Mini projeto — Gerenciador de Tarefas
#
# ==========================================


# ==========================================
# 1️⃣ MANIPULAÇÃO DE ARQUIVOS
# ==========================================

print("\n=== MANIPULAÇÃO DE ARQUIVOS ===")

# Escrever em um arquivo
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha.\n")
    arquivo.write("Segunda linha de texto.")

# Ler o arquivo inteiro
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)

# Ler linha por linha
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print("Linha:", linha.strip())

# Adicionar conteúdo (modo append)
with open("exemplo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nTerceira linha adicionada!")


# ==========================================
# 2️⃣ TRATAMENTO DE ERROS
# ==========================================

print("\n=== TRATAMENTO DE ERROS ===")

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("⚠️ Valor inválido! Digite um número inteiro.")
except ZeroDivisionError:
    print("❌ Erro: divisão por zero!")
except Exception as e:
    print("Erro inesperado:", e)
else:
    print("✅ Cálculo realizado com sucesso.")
finally:
    print("Bloco finally executado — fim do tratamento.")


# ==========================================
# 3️⃣ FUNÇÕES AVANÇADAS E LAMBDA
# ==========================================

print("\n=== FUNÇÕES AVANÇADAS ===")

def filtrar_pares(numeros):
    return list(filter(lambda n: n % 2 == 0, numeros))

def dobrar_valores(numeros):
    return list(map(lambda n: n * 2, numeros))

def somar_todos(numeros):
    from functools import reduce
    return reduce(lambda x, y: x + y, numeros)

lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)
print("Pares:", filtrar_pares(lista))
print("Dobro:", dobrar_valores(lista))
print("Soma total:", somar_todos(lista))


# ==========================================
# 4️⃣ POO BÁSICA — CLASSES E OBJETOS
# ==========================================

print("\n=== POO BÁSICA ===")

class Pessoa:
    """Classe simples representando uma pessoa."""

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Nikollas", 21)
p2 = Pessoa("Ana", 19)

p1.apresentar()
p2.apresentar()


# ==========================================
# 5️⃣ MINI PROJETO — GERENCIADOR DE TAREFAS
# ==========================================

print("\n=== MINI PROJETO: GERENCIADOR DE TAREFAS ===")

import json
from typing import List

class Tarefa:
    """Representa uma tarefa com título e status."""

    def __init__(self, titulo: str):
        self.titulo = titulo
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def to_dict(self):
        return {"titulo": self.titulo, "concluida": self.concluida}


class GerenciadorTarefas:
    """Gerencia a criação, listagem e conclusão de tarefas."""

    ARQUIVO = "tarefas.json"

    def __init__(self):
        self.tarefas: List[Tarefa] = self.carregar_tarefas()

    def carregar_tarefas(self) -> List[Tarefa]:
        try:
            with open(self.ARQUIVO, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                return [Tarefa(t["titulo"]) for t in dados]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("⚠️ Erro ao ler o arquivo de tarefas, iniciando vazio.")
            return []

    def salvar_tarefas(self):
        with open(self.ARQUIVO, "w", encoding="utf-8") as arq:
            json.dump([t.to_dict() for t in self.tarefas], arq, indent=2, ensure_ascii=False)

    def criar_tarefa(self, titulo: str):
        if not titulo.strip():
            print("⚠️ O título não pode estar vazio.")
            return
        nova = Tarefa(titulo)
        self.tarefas.append(nova)
        self.salvar_tarefas()
        print(f"✅ Tarefa '{titulo}' criada com sucesso.")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        for i, t in enumerate(self.tarefas, start=1):
            status = "✅" if t.concluida else "❌"
            print(f"{i}. {t.titulo} [{status}]")

    def concluir_tarefa(self, indice: int):
        if 0 < indice <= len(self.tarefas):
            self.tarefas[indice - 1].concluir()
            self.salvar_tarefas()
            print(f"🎯 Tarefa '{self.tarefas[indice - 1].titulo}' concluída!")
        else:
            print("⚠️ Índice inválido.")


def menu_gerenciador():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            gerenciador.criar_tarefa(titulo)
        elif opcao == "2":
            gerenciador.listar_tarefas()
        elif opcao == "3":
            gerenciador.listar_tarefas()
            indice = int(input("Número da tarefa a concluir: "))
            gerenciador.concluir_tarefa(indice)
        elif opcao == "4":
            print("Encerrando... 👋")
            break
        else:
            print("Opção inválida!")

# Descomente para testar o menu:
# if __name__ == "__main__":
#     menu_gerenciador()
