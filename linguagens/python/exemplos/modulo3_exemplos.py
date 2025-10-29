# ==========================================
# 🧩 DevKickStart — Python Módulo 3 (Avançado)
# Exemplos práticos organizados por tema
# ==========================================
#
# Conteúdo:
#
# 1. POO Avançada (abstração, herança, polimorfismo)
# 2. Encapsulamento, propriedades e dataclasses
# 3. Exceções personalizadas + logging
# 4. Módulos e pacotes (organização de projeto)
# 5. Tipagem estática (type hints) e mypy
# 6. Consumo de API (requests)
# 7. Testes automatizados (pytest)
# 8. Mini-projeto avançado — Gestor de Tarefas (JSON + POO)
#
#  ==========================================

from __future__ import annotations
from typing import List, Dict, Optional, Iterable, Protocol, runtime_checkable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import json
import logging
from datetime import datetime
import os

# Configuração básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(name)s | %(message)s",
    datefmt="%H:%M:%S"
)
log = logging.getLogger("DevKickStart.M3")

print("\n=== MÓDULO 3 — CONTEÚDOS AVANÇADOS ===")


# ==========================================
# 1️⃣ POO AVANÇADA — Abstração, Herança, Polimorfismo
# ==========================================

print("\n--- 1) POO Avançada: abstração, herança, polimorfismo ---")

class Notificavel(ABC):
    """Interface abstrata: qualquer coisa que 'notifica' precisa implementar enviar()."""
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        ...

class EmailNotifier(Notificavel):
    def __init__(self, email: str) -> None:
        self.email = email

    def enviar(self, mensagem: str) -> None:
        print(f"[EMAIL → {self.email}] {mensagem}")

class ConsoleNotifier(Notificavel):
    def enviar(self, mensagem: str) -> None:
        print(f"[CONSOLE] {mensagem}")

def avisar(notificador: Notificavel, texto: str) -> None:
    """Polimorfismo: aceita qualquer objeto que implemente Notificavel."""
    notificador.enviar(texto)

avisar(ConsoleNotifier(), "Tarefa concluída com sucesso.")
avisar(EmailNotifier("aluno@devkickstart.io"), "Bem-vindo ao módulo avançado!")


# ==========================================
# 2️⃣ ENCAPSULAMENTO, PROPRIEDADES E DATACLASSES
# ==========================================

print("\n--- 2) Encapsulamento, propriedades e dataclasses ---")

@dataclass
class Produto:
    nome: str
    _preco: float = field(repr=False)  # oculto no repr, por estética

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Preço deve ser positivo.")
        self._preco = valor

p = Produto("Mouse Gamer", 150.0)
print("Produto:", p.nome, "| Preço:", p.preco)
p.preco = 199.9
print("Preço atualizado:", p.preco)


# ==========================================
# 3️⃣ EXCEÇÕES PERSONALIZADAS + LOGGING
# ==========================================

print("\n--- 3) Exceções personalizadas + logging ---")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo: float, valor: float) -> None:
        super().__init__(f"Saldo insuficiente: {saldo:.2f} < {valor:.2f}")
        self.saldo = saldo
        self.valor = valor

class Conta:
    def __init__(self, titular: str, saldo: float = 0.0) -> None:
        self.titular = titular
        self._saldo = saldo

    def sacar(self, valor: float) -> None:
        log.info("Solicitado saque de %.2f por %s", valor, self.titular)
        if valor > self._saldo:
            log.error("Falha no saque: saldo=%.2f, valor=%.2f", self._saldo, valor)
            raise SaldoInsuficienteError(self._saldo, valor)
        self._saldo -= valor
        log.info("Saque OK. Saldo atual: %.2f", self._saldo)

    @property
    def saldo(self) -> float:
        return self._saldo

conta = Conta("Nikollas", 100.0)
try:
    conta.sacar(150.0)
except SaldoInsuficienteError as e:
    print("Erro de saque:", e)


# ==========================================
# 4️⃣ MÓDULOS E PACOTES (organização)
# ==========================================

print("\n--- 4) Módulos e Pacotes (organização sugerida) ---")
# Estrutura sugerida (exemplo):
# meu_app/
# ├── app.py                # ponto de entrada
# ├── services/
# │   ├── __init__.py
# │   ├── notificacao.py    # classes Notificavel, EmailNotifier, etc.
# │   └── tarefas.py        # classes de Tarefa e Gerenciador
# └── tests/
#     └── test_tarefas.py   # testes com pytest
print("Ver estrutura comentada no código. Organização por camadas e responsabilidades.")


# ==========================================
# 5️⃣ TIPAGEM ESTÁTICA (type hints) E MYPY
# ==========================================

print("\n--- 5) Type hints e mypy ---")

def dividir(a: float, b: float) -> float:
    """Divide a por b; levanta ZeroDivisionError se b = 0."""
    return a / b

print("dividir(10.0, 2.0) =", dividir(10.0, 2.0))
# Rodando tipo-checker (fora do Python, no terminal):
#   mypy linguagens/python/exemplos/modulo3_exemplos.py


# ==========================================
# 6️⃣ CONSUMO DE API (requests)
# ==========================================

print("\n--- 6) Consumo de API (requests) ---")
# Observação: requer `pip install requests`.
try:
    import requests
    resp = requests.get("https://api.github.com/users/imnikollasdev", timeout=10)
    if resp.status_code == 200:
        dados = resp.json()
        print(f"GitHub: {dados.get('login')} | Repositórios públicos: {dados.get('public_repos')}")
    else:
        print("Falha ao consultar GitHub:", resp.status_code)
except Exception as e:
    print("Não foi possível realizar a requisição HTTP (sem internet ou requests ausente).", e)


# ==========================================
# 7️⃣ TESTES AUTOMATIZADOS (pytest)
# ==========================================

print("\n--- 7) Testes automatizados (pytest) — exemplo de layout ---")
# Arquivo: calculadora.py
def soma(a: int, b: int) -> int:
    return a + b

# Arquivo: test_calculadora.py
# ---------------------------------
# from calculadora import soma
# def test_soma():
#     assert soma(2, 3) == 5
# ---------------------------------
print("Exemplo de teste exibido em comentários. Rode: pytest -q")


# ==========================================
# 8️⃣ MINI-PROJETO AVANÇADO — GESTOR DE TAREFAS
# ==========================================

print("\n--- 8) Mini-projeto: Gestor de Tarefas (avançado) ---")

class ValidacaoError(Exception):
    """Erros de validação de domínio."""

@runtime_checkable
class Persistencia(Protocol):
    def carregar(self) -> List[Dict]: ...
    def salvar(self, dados: List[Dict]) -> None: ...

class PersistenciaJSON:
    """Persistência simples em JSON."""
    def __init__(self, caminho: str) -> None:
        self.caminho = caminho

    def carregar(self) -> List[Dict]:
        if not os.path.exists(self.caminho):
            return []
        try:
            with open(self.caminho, "r", encoding="utf-8") as arq:
                return json.load(arq)
        except json.JSONDecodeError:
            log.warning("JSON inválido; iniciando vazio.")
            return []

    def salvar(self, dados: List[Dict]) -> None:
        with open(self.caminho, "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=2, ensure_ascii=False)

@dataclass
class Tarefa:
    titulo: str
    prioridade: int = 3            # 1=alta, 2=media, 3=baixa
    deadline: Optional[str] = None # ISO date: "YYYY-MM-DD"
    concluida: bool = False
    criada_em: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def __post_init__(self) -> None:
        if not self.titulo or not self.titulo.strip():
            raise ValidacaoError("Titulo da tarefa é obrigatório.")
        if self.prioridade not in (1, 2, 3):
            raise ValidacaoError("Prioridade deve ser 1, 2 ou 3.")
        if self.deadline:
            try:
                datetime.fromisoformat(self.deadline)
            except ValueError:
                raise ValidacaoError("Deadline deve estar no formato YYYY-MM-DD.")

    def concluir(self) -> None:
        self.concluida = True

    def to_dict(self) -> Dict:
        return {
            "titulo": self.titulo,
            "prioridade": self.prioridade,
            "deadline": self.deadline,
            "concluida": self.concluida,
            "criada_em": self.criada_em,
        }

class GerenciadorTarefas:
    def __init__(self, storage: Persistencia) -> None:
        self.storage = storage
        self._tarefas: List[Tarefa] = [Tarefa(**d) for d in storage.carregar()]

    # CRUD básico
    def criar(self, titulo: str, prioridade: int = 3, deadline: Optional[str] = None) -> None:
        tarefa = Tarefa(titulo=titulo, prioridade=prioridade, deadline=deadline)
        self._tarefas.append(tarefa)
        self._commit()
        log.info("Tarefa criada: %s", tarefa.titulo)

    def listar(self, *, somente_abertas: bool = False) -> List[Tarefa]:
        tarefas = [t for t in self._tarefas if not t.concluida] if somente_abertas else list(self._tarefas)
        return sorted(tarefas, key=lambda t: (t.concluida, t.prioridade, t.deadline or "9999-12-31", t.criada_em))

    def concluir(self, indice: int) -> None:
        if not 1 <= indice <= len(self._tarefas):
            raise ValidacaoError("Índice inválido.")
        self._tarefas[indice - 1].concluir()
        self._commit()
        log.info("Tarefa concluída: %s", self._tarefas[indice - 1].titulo)

    def excluir(self, indice: int) -> None:
        if not 1 <= indice <= len(self._tarefas):
            raise ValidacaoError("Índice inválido.")
        removida = self._tarefas.pop(indice - 1)
        self._commit()
        log.info("Tarefa removida: %s", removida.titulo)

    # Utilidades
    def _commit(self) -> None:
        self.storage.salvar([t.to_dict() for t in self._tarefas])

    def imprimir(self, itens: Optional[Iterable[Tarefa]] = None) -> None:
        itens = itens or self._tarefas
        if not itens:
            print("Nenhuma tarefa.")
            return
        print("\n# Tarefas")
        for i, t in enumerate(itens, 1):
            status = "✅" if t.concluida else "❌"
            pri = {1: "Alta", 2: "Média", 3: "Baixa"}[t.prioridade]
            dl = t.deadline or "—"
            print(f"{i:02d}. [{status}] {t.titulo} | Prioridade: {pri} | Deadline: {dl} | Criada: {t.criada_em}")

# --- Menu CLI (opcional) ---
def menu():
    storage = PersistenciaJSON("tarefas.json")
    g = GerenciadorTarefas(storage)

    while True:
        print("\n=== GESTOR DE TAREFAS (Avançado) ===")
        print("1. Criar tarefa")
        print("2. Listar tarefas (todas)")
        print("3. Listar tarefas (abertas)")
        print("4. Concluir tarefa")
        print("5. Excluir tarefa")
        print("6. Sair")
        op = input("Escolha: ").strip()

        try:
            if op == "1":
                titulo = input("Título: ").strip()
                pri = int(input("Prioridade (1=Alta, 2=Média, 3=Baixa): ").strip() or "3")
                dl = input("Deadline (YYYY-MM-DD) [opcional]: ").strip() or None
                g.criar(titulo, prioridade=pri, deadline=dl)
            elif op == "2":
                g.imprimir(g.listar())
            elif op == "3":
                g.imprimir(g.listar(somente_abertas=True))
            elif op == "4":
                g.imprimir()
                idx = int(input("Número da tarefa a concluir: "))
                g.concluir(idx)
            elif op == "5":
                g.imprimir()
                idx = int(input("Número da tarefa a excluir: "))
                g.excluir(idx)
            elif op == "6":
                print("Encerrando... 👋")
                break
            else:
                print("Opção inválida.")
        except (ValueError, ValidacaoError) as e:
            print("⚠️ Erro:", e)

# Para usar o menu interativo, descomente:
# if __name__ == "__main__":
#     menu()
