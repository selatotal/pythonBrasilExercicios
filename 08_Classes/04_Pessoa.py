from pprint import pprint


class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        if (peso > self.peso):
            self.peso = 0
        else:
            self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def envelhecer(self, anos):
        anosAntes = self.idade
        self.idade += anos
        if (anosAntes < 25):
            if (self.idade < 25):
                self.crescer(anos * 0.5)
            else:
                self.crescer((25 - anosAntes) * 0.5)


# TESTE DA CLASSE
alberto = Pessoa('Alberto', 20, 87.0, 190)
pprint(vars(alberto))
alberto.engordar(1)
pprint(vars(alberto))
alberto.emagrecer(2)
pprint(vars(alberto))
alberto.crescer(3)
pprint(vars(alberto))
alberto.envelhecer(7)
pprint(vars(alberto))
