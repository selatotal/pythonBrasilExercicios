salario = 1000.0
percentual = 1.5
ano = 1996

while (ano <= 2014):
    print 'Ano (%i) Percentual (%.2f) Salario (%.2f)' %\
        (ano, percentual, salario)
    salario += (salario * (percentual / 100.0))
    percentual *= 2
    ano += 1

print 'Salario atual do funcionario: %.2f' % (salario)
