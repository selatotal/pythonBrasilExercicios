numeros = []
pares = []
impares = []

for i in range(0, 20):
    numero = int(raw_input('Informe um numero: '))
    numeros.append(numero)
    if (numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)

print numeros
print pares
print impares
