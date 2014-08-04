# Declara um vetor com 23 posicoes inicializando ele com o valor zero
sistemasOperacionais = (
    'Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro')
votosSistemas = [0] * 6
opcao = -1
totalVotos = 0
print 'Qual o melhor Sistema Operacional para uso em servidores?'
print '\nAs possiveis respostas sao:\n'

i = 0
for sistema in sistemasOperacionais:
    print '%d- %s' % (i + 1, sistemasOperacionais[i])
    i += 1

while (opcao != 0):
    opcao = int(raw_input('Sistema escolhido (0=fim): '))
    if (opcao < 0) or (opcao > 23):
        print 'Informe um valor entre 1 e 6 ou 0 para sair!'
        continue
    if (opcao != 0):
        votosSistemas[opcao - 1] += 1
        totalVotos += 1

print 'Sistema Operacional   Votos   %'
print '-------------------   -----   ------'
i = 0
maiorVoto = 0
for sistema in sistemasOperacionais:
    print '%-21s %5d   %2.2f' %\
        (sistemasOperacionais[i], votosSistemas[i],
         votosSistemas[i] / float(totalVotos) * 100)
    if (votosSistemas[i] > votosSistemas[maiorVoto]):
        maiorVoto = i
    i += 1
print '-------------------   -----'
print 'Total                   %3d' % totalVotos

print 'O sistema operacional mais votado foi o %s, com %d, correspondendo a '\
    '%.2f%% dos votos.' %\
    (sistemasOperacionais[maiorVoto], votosSistemas[maiorVoto],
        votosSistemas[maiorVoto] / float(totalVotos) * 100)
