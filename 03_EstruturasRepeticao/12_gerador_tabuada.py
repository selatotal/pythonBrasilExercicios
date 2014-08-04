numero = int(raw_input('Informe o numero que voce quer ver a tabuada: '))

print 'Tabuada de', numero, ':'
for i in range(1, 11):
    print numero, 'X', i, '=', (numero * i)
