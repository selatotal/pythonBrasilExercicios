a = []
for i in range(0, 10):
    a.append(int(raw_input('Informe um numero: ')))

somaQuadrados = 0
for numero in a:
    somaQuadrados += (numero * numero)

print 'A soma dos quadrados dos numeros lidos eh %d' % somaQuadrados
