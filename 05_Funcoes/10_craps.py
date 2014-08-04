import random


def JogaDadosCraps():
    jogada = random.randint(2, 12)
    return jogada

# Fluxo Principal

quantidadeJogadas = 1
acabou = False
ponto = 0

while (not acabou):
    jogada = JogaDadosCraps()
    print 'Jogada %d: %d' % (quantidadeJogadas, jogada)

    if (quantidadeJogadas == 1):
        if (jogada == 2) or (jogada == 3) or (jogada == 12):
            print 'Craps! Voce Perdeu!'
            acabou = True
        elif (jogada == 7) or (jogada == 11):
            print 'Voce Ganhou!'
            acabou = True
        else:
            ponto = jogada
            print 'Seu ponto eh %d' % ponto
    else:
        if (jogada == 7):
            print 'Voce Perdeu!'
            acabou = True
        elif (jogada == ponto):
            print 'Voce Ganhou!'
            acabou = True
    quantidadeJogadas += 1
