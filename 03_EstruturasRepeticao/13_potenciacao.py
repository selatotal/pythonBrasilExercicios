base = int(raw_input('Informe o valor da base: '))
expoente = 0
while (expoente <= 0):
    expoente = int(raw_input('Informe o valor do expoente: '))
    if (expoente <= 0):
        print 'O expoente deve ser positivo!'

potencia = 1
for i in range(1, expoente + 1):
    potencia *= base

print base, 'elevada a', expoente, '=', potencia
