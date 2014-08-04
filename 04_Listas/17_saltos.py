textoSaltos = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
nomeAtleta = ' '
atletas = {}

while (nomeAtleta != ''):
    nomeAtleta = raw_input('Atleta: ')
    if (nomeAtleta != ''):
        saltos = []
        for i in textoSaltos:
            saltos.append(float(raw_input('%s Salto: ' % i)))
        atletas[nomeAtleta] = saltos

print '\nResultado Final:'
for (nomeAtleta, saltos) in atletas.items():
    print 'Atleta: %s' % nomeAtleta
    print 'Saltos: ', saltos
    somaSaltos = 0.0
    for salto in saltos:
        somaSaltos += salto
    print 'Media dos Saltos %.2f m' % (somaSaltos / float(len(textoSaltos)))
