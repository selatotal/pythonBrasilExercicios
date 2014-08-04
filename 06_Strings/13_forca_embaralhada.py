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
palavraAdivinhada = random.sample(palavraEscolhida, len(palavraEscolhida))
for i in palavraAdivinhada:
    print '%s' % i,
print

palavra = raw_input('Digite qual eh a palavra: ').upper()

if (palavra == palavraEscolhida):
    print 'Voce acertou!'
else:
    print 'Voce perdeu!'
    print 'A palavra era %s' % palavraEscolhida
