salarios = []
salarioFuncionario = -1
print 'Projecao de Gastos com Abono'
print '============================\n'

while (salarioFuncionario != 0):
    salarioFuncionario = float(raw_input('Salario: '))
    if (salarioFuncionario < 0):
        print 'Informe um valor maior que 0 ou 0 para sair!'
        continue
    if (salarioFuncionario != 0):
        salarios.append(salarioFuncionario)

print 'Salario\tAbono'

totalAbono = 0.0
totalPiso = 0

for salario in salarios:
    abono = salario * 0.2
    if (abono < 100):
        abono = 100.0
        totalPiso += 1
    totalAbono += abono
    if ('maiorAbono' not in vars()) or (abono > maiorAbono):
        maiorAbono = abono
    print 'R$ %.2f\tR$%.2f' % (salario, abono)

print 'Foram processados %d votos' % len(salarios)
print 'Total gasto com abonos: %.2f' % totalAbono
print 'Valor minimo pago a %d colaboradores' % totalPiso
print 'Maior valor de abono pago: %.2f' % maiorAbono
