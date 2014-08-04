salario = float(raw_input('Informe o valor do salario do colaborador: '))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100.0)
novoSalario = salario + aumento

print 'Salario antes do reajuste:', salario
print 'Percentual de aumento:', percentual, '%'
print 'Valor do aumento:', aumento
print 'Novo Salario:', novoSalario
