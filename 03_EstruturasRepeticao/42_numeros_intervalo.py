numero = 0

intervalo025 = 0
intervalo2650 = 0
intervalo5175 = 0
intervalo76100 = 0

while (numero >= 0):
    numero = int(raw_input('Informe um numero: '))

    if (numero >= 0):
        if (numero <= 25):
            intervalo025 += 1
        elif (numero <= 51):
            intervalo2650 += 1
        elif (numero <= 75):
            intervalo5175 += 1
        elif (numero <= 100):
            intervalo76100 += 1

print '%d numeros no intervalo [0-25]' % (intervalo025)
print '%d numeros no intervalo [26-50]' % (intervalo2650)
print '%d numeros no intervalo [51-75]' % (intervalo5175)
print '%d numeros no intervalo [75-100]' % (intervalo76100)
