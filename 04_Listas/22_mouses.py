idMouse = -1
defeitos = ('1 - Necessita de Esfera',
            '2 - Necessita de limpeza',
            '3 - Necessita troca de cabo ou conector',
            '4 - Quebrado ou inutilizado')
totalDefeitos = [0] * 4
totalMouses = 0

for i in defeitos:
    print '%s' % i

while (idMouse != 0):
    idMouse = int(raw_input('Identificador do Mouse: '))
    if (idMouse != 0):
        defeito = int(raw_input('Codigo do defeito: '))
        totalDefeitos[defeito - 1] += 1
        totalMouses += 1

print 'Quantidade de mouses: %d ' % totalMouses

print 'Situacao\tQuantidade\tPercentual'
for i in range(0, len(defeitos)):
    print '%s\t%d\t%.2f' %\
        (defeitos[i], totalDefeitos[i], totalDefeitos[i] /
            float(totalMouses) * 100)
