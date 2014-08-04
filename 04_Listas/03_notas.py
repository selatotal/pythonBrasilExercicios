notas = []
for i in range(0, 4):
    notas.append(float(raw_input('Informe uma nota: ')))

soma = 0.0
print '\nNotas Digitadas:'
for i in range(0, 4):
    print 'Nota %d: %.2f' % (i, notas[i])
    soma += notas[i]

print 'Media das notas: %.2f' % (soma / 4.0)
