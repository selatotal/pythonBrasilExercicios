print 'Comparativo de Consumo de Combustivel'

veiculos = []
consumo = []
preco = 2.25

for i in range(1, 6):
    veiculos.append(raw_input('Veiculo %d: ' % i))
    consumo.append(float(raw_input('Km por litro: ')))

print 'Relatorio Final'

for i in range(0, 5):
    custo = 1000 / consumo[i]
    gasto = custo * preco
    print '%d - %s - %.2f - %.1f litros - R$ %.2f' %\
        (i + 1, veiculos[i], consumo[i], custo, gasto)
    if ('menorConsumo' not in vars()) or (consumo[i] > consumo[menorConsumo]):
        menorConsumo = i

print 'O menor consumo eh do %s' % veiculos[menorConsumo]
