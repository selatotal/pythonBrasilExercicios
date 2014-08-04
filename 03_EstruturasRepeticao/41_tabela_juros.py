divida = float(raw_input('Informe o valor da divida: '))

print\
    'Valor da divida\tValor dos Juros\t'\
    'Quantidade de Parcelas\tValor da Parcela'
juros = 0
for i in [1, 3, 6, 9, 12]:
    valorJuros = (divida * (juros / 100.0))
    valorDivida = divida + valorJuros
    valorParcela = valorDivida / float(i)
    print 'R$ %.2f\tR$ %.2f\t%i\tR$ %.2f' %\
        (valorDivida, valorJuros, i, valorParcela)
    if (i == 1):
        juros = 10
    else:
        juros += 5
