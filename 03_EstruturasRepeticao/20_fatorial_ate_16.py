quantidade = 0
while (quantidade <= 0):
    quantidade = int(raw_input('Voce quer a fatorial de quantos numeros: '))
    if (quantidade <= 0):
        print 'Quantidade deve ser positiva!'

for i in range(0, quantidade):
    termo = 0
    while (termo <= 0) or (termo > 16):
        termo = int(raw_input('Voce quer o fatorial de qual termo: '))
        if (termo <= 0):
            print 'O termo deve ser positivo!'
        if (termo > 16):
            print 'O termo deve ser menor que 16'

    fatorial = 1
    for i in range(1, termo + 1):
        fatorial *= i

    print fatorial
