numeros = []
for i in range(0, 4):
    numeros.append(int(raw_input('Informe um numero inteiro: ')))

soma = 0
multiplicacao = 1
for i in numeros:
    soma += i
    multiplicacao *= i

print numeros
print 'Soma dos numeros: %d' % soma
print 'Multiplicacao dos numeros: %d' % multiplicacao
