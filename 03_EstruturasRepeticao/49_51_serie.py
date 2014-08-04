termos = int(raw_input('Informe a quantidade de termos que deseja: '))

s = 0.0
denominador = 1
for i in range(1, termos + 1):
    s += i / denominador
    denominador += 2

print 'Resultado: %.2f' % s
