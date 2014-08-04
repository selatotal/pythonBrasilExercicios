class Carro:

    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel = 0

    def adicionarGasolina(self, quantidade):
        self.qtdeCombustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.qtdeCombustivel -= gasto

    def obterGasolina(self):
        print self.qtdeCombustivel

# TESTE DA CLASSE
meuFusca = Carro(15)
# 15 quilometros por litro de combustivel.
meuFusca.adicionarGasolina(20)
# abastece com 20 litros de combustivel.
meuFusca.andar(100)
# anda 100 quilometros.
meuFusca.obterGasolina()        # Imprime o combustivel que resta no tanque.
