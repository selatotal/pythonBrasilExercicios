numero = 0
while (numero <= 0):
    numero = int(raw_input('Voce quer ver se qual numero eh primo: '))
    if (numero <= 0):
        print 'O numero deve ser positivo!'

primo = True
for i in range(2, numero / 2 + 1):
    if (numero % i == 0):
        primo = False
        break

if (primo):
    print 'O numero eh primo'
else:
    print 'O numero nao eh primo'
    print 'Ele eh divisivel por',
    for i in range(1, numero + 1):
        if (numero % i == 0):
            print i,
