preco1 = int(raw_input('Informe o primeiro preco: '))
preco2 = int(raw_input('Informe o segundo preco: '))
preco3 = int(raw_input('Informe o terceiro preco: '))

if (preco1 == preco2) and (preco1 == preco3):
    print 'Pode comprar qualquer um, ja que os precos sao iguais.'
elif (num1 < num2) and (num1 < num3):
    print 'Compre pelo primeiro preco'
elif (num2 < num3):
    print 'Compre pelo segundo preco'
else:
    print 'Compre pelo terceiro preco'
