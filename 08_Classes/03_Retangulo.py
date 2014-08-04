class Retangulo:

    def __init__(self, base, altura):
        self.setBase(base)
        self.setAltura(altura)

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def setAltura(self, altura):
        self.altura = altura

    def getAltura(self):
        return self.altura

    def calculaArea(self):
        return self.base * self.altura

    def calculaPerimetro(self):
        return 2 * self.base + 2 * self.altura

# TESTE DA CLASSE
base = int(raw_input('Informe o valor da base: '))
altura = int(raw_input('Informe o valor da altura: '))
retangulo = Retangulo(base, altura)
print 'A area do retangulo eh: %d' % retangulo.calculaArea()
print 'O perimetro do retangulo eh: %d' % retangulo.calculaPerimetro()
