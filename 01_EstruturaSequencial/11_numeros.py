import math

numInt1 = int(raw_input('Informe um numero inteiro: '))
numInt2 = int(raw_input('Informe outro numero inteiro: '))
numReal = float(raw_input('Informe um numero real: '))

print 'O dobro do primeiro vezes a metade do segundo eh', \
    (2 * numInt1) / (numInt2 / 2.0)
print 'A soma do triplo do primeiro com o terceiro eh', (3 * numInt1) + numReal
print 'O terceiro elevado ao cubo eh', math.pow(numReal, 3)
