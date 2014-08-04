valorPorHora = float(raw_input('Quanto voce ganha por hora: '))
horasTrabalhadas = float(raw_input('Quantas horas voce trabalhou no mes: '))

salarioBruto = valorPorHora * horasTrabalhadas
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print 'Salario Bruto:', salarioBruto
print 'Imposto de Renda:', impostoRenda
print 'INSS:', inss
print 'Sindicato:', sindicato
print 'Salario Liquido:', salarioLiquido
