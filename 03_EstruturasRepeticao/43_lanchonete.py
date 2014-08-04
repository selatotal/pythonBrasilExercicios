print 'Especificacao   Codigo  Preco'
print 'Cachorro Quente 100     R$ 1,20'
print 'Bauru Simples   101     R$ 1,30'
print 'Bauru com Ovo   102     R$ 1,50'
print 'Hamburger       103     R$ 1,20'
print 'Cheeseburger    104     R$ 1,30'
print 'Refrigerante    105     R$ 1,00'

codigo = 100
valorTotal = 0
while (codigo >= 100 and codigo <= 105):
    codigo = int(
        raw_input(
            'Informe o codigo do produto ou um codigo invalido para encerrar: '
        ))
    if (codigo >= 100 and codigo <= 105):
        quantidade = int(raw_input('Informe a quantidade: '))
        if (codigo == 100):
            valorItem = 1.20 * quantidade
        elif (codigo == 101):
            valorItem = 1.30 * quantidade
        elif (codigo == 102):
            valorItem = 1.50 * quantidade
        elif (codigo == 103):
            valorItem = 1.20 * quantidade
        elif (codigo == 104):
            valorItem = 1.30 * quantidade
        elif (codigo == 105):
            valorItem = 1.0 * quantidade
        print 'Valor do item: %.2f' % valorItem
        valorTotal += valorItem

print 'Valor Total: %.2f' % (valorTotal)
