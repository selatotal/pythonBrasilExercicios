precoPao = float(raw_input('Preco do pao: '))

print 'Panificadora Pao de Ontem - Tabela de precos'
for i in range(1, 51):
    print '%d - R$ %.2f' % (i, i * precoPao)
