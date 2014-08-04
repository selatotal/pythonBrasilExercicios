import random

# Abre o arquivo para leitura
arquivoEntrada = open('11_palavras.txt', 'r')

# Coloca todas as linhas em memoria
palavras = arquivoEntrada.readlines()

# Fecha o arquivo
arquivoEntrada.close()

palavraEscolhida = palavras[
    random.randint(0, len(palavras) - 1)].upper().strip()
tamanhoPalavra = len(palavraEscolhida)
palavraAdivinhada = ['_'] * tamanhoPalavra

numTentativas = 0
numErros = 0

while (''.join(palavraAdivinhada) != palavraEscolhida) and (numErros < 6):

    letra = raw_input('Digite uma letra: ').upper()
    numTentativas += 1
    acertou = False

    print 'A palavra eh: ',
    for i in range(0, tamanhoPalavra):
        if (palavraEscolhida[i] == letra):
            palavraAdivinhada[i] = letra
            acertou = True
        print '%s' % palavraAdivinhada[i],

    print
    if (not acertou):
        numErros += 1
        print 'Voce errou pela %da. vez.' % numErros

if (numErros < 6):
    print 'Voce acertou!'
else:
    print 'Voce perdeu!'
    print 'A palavra era %s' % palavraEscolhida
