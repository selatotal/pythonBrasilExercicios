# Declara um vetor com 23 posicoes inicializando ele com o valor zero
votosAtletas = [0] * 23
numeroAtleta = -1
totalVotos = 0
print 'Enquete: Quem foi o melhor jogador?'

while (numeroAtleta != 0):
    numeroAtleta = int(raw_input('Numero do jogador (0=fim): '))
    if (numeroAtleta < 0) or (numeroAtleta > 23):
        print 'Informe um valor entre 1 e 23 ou 0 para sair!'
        continue
    if (numeroAtleta != 0):
        votosAtletas[numeroAtleta - 1] += 1
        totalVotos += 1

print 'Resultado da votacao:'

print 'Foram computados %d votos' % totalVotos
print 'Jogador\tVotos\t%%'
contador = 1
melhorJogador = 0
for votosAtleta in votosAtletas:
    if (votosAtleta > 0):
        print '%d\t%d\t%.2f%%' %\
              (contador, votosAtleta, votosAtleta / float(totalVotos) * 100)
        if (votosAtleta > votosAtletas[melhorJogador]):
            melhorJogador = contador - 1
    contador += 1

print 'O melhor jogador foi o numero %d, com %d votos, correspondendo a '\
    '%.2f do total de votos' %\
    (melhorJogador + 1, votosAtletas[melhorJogador],
        votosAtletas[melhorJogador] / float(totalVotos) * 100)
