from typing import List
from conta import Conta
from transacao import Transacao


class Cliente:
    endereco: str
    contas: List[Conta]

    def __init__(self, endereco: str, contas: List[Conta]):
        self.endereco = endereco
        self.contas = contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        pass

    def adicionar_conta(self, conta: Conta) -> None:
        self.contas.append(conta)
