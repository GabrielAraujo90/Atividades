#Atividade09

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        if super().sacar(valor + taxa):
            return True
        else:
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        else:
            return False


conta = ContaBancaria("João", 1000)
print("Saldo inicial:", conta.saldo)
conta.depositar(500)
print("Saldo após depósito:", conta.saldo)
conta.sacar(300)
print("Saldo após saque:", conta.saldo)


conta_poupanca = ContaPoupanca("Maria", 1500)
print("Saldo inicial da conta poupança:", conta_poupanca.saldo)
conta_poupanca.sacar(100)
print("Saldo após saque na conta poupança:", conta_poupanca.saldo)


conta_corrente = ContaCorrente("Pedro", 2000, 1000)
print("Saldo inicial da conta corrente:", conta_corrente.saldo)
conta_corrente.sacar(2500)
print("Saldo após saque na conta corrente:", conta_corrente.saldo)
