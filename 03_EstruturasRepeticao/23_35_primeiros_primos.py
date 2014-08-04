quantidade = 0
while (quantidade <= 0):
    quantidade = int(
        raw_input('Voce quer saber os primeiros quantos numeros: '))
    if (quantidade <= 0):
        print 'A quandidade deve ser positiva!'

quantidadeDivisoes = 0
for numero in range(1, quantidade + 1):
    primo = True
    for i in range(2, numero / 2 + 1):
        quantidadeDivisoes += 1
        if (numero % i == 0):
            primo = False
            break

    if (primo):
        print numero,

print '\nQuantidade de divisoes:', quantidadeDivisoes
