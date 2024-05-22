from cliente import Cliente
from historico import Historico


class Conta:
    saldo: float
    numero: int
    agencia: str
    cliente: Cliente
    historico: Historico

    def __init__(
            self, numero: int,
            agencia: str,
            cliente: Cliente,
            historico: Historico
          ):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0
        self.historico = historico

    @property
    def saldo(self) -> float:
        return self.saldo

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito de {valor}")

    def sacar(self, valor: float) -> None:
        if self.saldo < valor:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.historico.transacoes.append(f"Saque de {valor}")
