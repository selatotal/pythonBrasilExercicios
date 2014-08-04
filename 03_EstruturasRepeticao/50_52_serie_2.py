termos = int(raw_input('Informe a quantidade de termos que deseja: '))

s = 0.0
for i in range(1, termos + 1):
    s += 1 / i

print 'Resultado: %.2f' % s
