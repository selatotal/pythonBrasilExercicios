class Bola:

    'Classe para definir uma bola'

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print self.cor

# Teste da Classe
bola = Bola()
bola.trocaCor("Azul")
bola.mostraCor()
