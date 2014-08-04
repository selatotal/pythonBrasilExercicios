# Solicita os dados
valorPorHora = float(raw_input('Informe o valor da hora trabalhada: '))
quantidadeHoras =\
    float(raw_input('Informe a quantidade de horas trabalhadas no mes:'))

# Calcula o salario bruto
salarioBruto = valorPorHora * quantidadeHoras

# Calcula o imposto de renda
if (salarioBruto > 2500):
    aliquotaIR = 20
elif (salarioBruto > 1500):
    aliquotaIR = 10
elif (salarioBruto > 900):
    aliquotaIR = 5
else:
    aliquotaIR = 0

valorIR = salarioBruto * (aliquotaIR / 100.0)

# Calcula o valor para o sindicato
valorSindicato = salarioBruto * (3 / 100.0)

# Calcula o total de descontos
totalDescontos = valorIR + valorSindicato

# Calcula o valor do FGTS
valorFGTS = salarioBruto * (11 / 100.0)

# Calcula o salario liquido
salarioLiquido = salarioBruto - totalDescontos

# Imprime o resultado
print 'Salario Bruto: (', valorPorHora, '*', quantidadeHoras, '): R$',\
    salarioBruto
print '(-) IR (', aliquotaIR, '%): R$', valorIR
print '(-) Sindicato ( 3 %): R$', valorSindicato
print 'FGTS ( 11 %): R$', valorFGTS
print 'Total de Descontos: R$', totalDescontos
print 'Salario Liquido: R$', salarioLiquido
