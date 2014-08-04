nomeAtleta = ' '
somaNotas = 0

atleta = raw_input('Atleta: ')

for i in range(0, 7):

    nota = float(raw_input('Nota: '))
    somaNotas += nota

    if ('maiorNota' not in vars()) or (nota > maiorNota):
        maiorNota = nota

    if ('menorNota' not in vars()) or (nota < menorNota):
        menorNota = nota

somaNotas -= maiorNota
somaNotas -= menorNota

print '\nResultado final:'
print 'Atleta: %s' % nomeAtleta
print 'Melhor nota: %.2f' % maiorNota
print 'Pior nota: %.2f' % menorNota
print 'Media: %.2f' % (somaNotas / 5.0)
