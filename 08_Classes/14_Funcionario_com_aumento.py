class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)

# TESTE DA CLASSE
harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)
print 'Nome: %s' % harry.getNome()
print 'Salario: %.2f' % harry.getSalario()
