class ContaInvestimento:

    def __init__(self, numero, nomeCorrentista, taxaJuros, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))

# TESTE DA CLASSE

conta = ContaInvestimento(100, 'Tales', 10)
conta.deposito(1000)
print conta.saldo
conta.adicionaJuros()
print conta.saldo
conta.adicionaJuros()
print conta.saldo
conta.adicionaJuros()
print conta.saldo
conta.adicionaJuros()
print conta.saldo
conta.adicionaJuros()
print conta.saldo
