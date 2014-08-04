class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print 'Bucho:', self.bucho

    def digerir(self):
        if (len(self.bucho) > 0):
            self.bucho.pop(0)

# Teste
macaco1 = Macaco('Simao')
macaco2 = Macaco('Prego')

macaco1.comer('Maca')
macaco1.verBucho()
macaco1.comer('Banana')
macaco1.verBucho()
macaco1.comer('Abacaxi')
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()
macaco2.comer('Maca')
macaco2.comer('Banaca')
macaco2.comer(macaco1)
macaco2.verBucho()
