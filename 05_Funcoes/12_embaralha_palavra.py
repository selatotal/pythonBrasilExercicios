import random


def embaralhaPalavra(palavra):
    tamanho = len(palavra)
    arrayPos = range(0, tamanho)

    for i in range(0, tamanho):
        pos1 = random.randint(0, tamanho - 1)
        pos2 = random.randint(0, tamanho - 1)

        aux = arrayPos[pos1]
        arrayPos[pos1] = arrayPos[pos2]
        arrayPos[pos2] = aux

    retorno = ''
    for i in arrayPos:
        retorno += palavra[i]

    return retorno.upper()

# Fluxo Principal
palavra = raw_input('Informe uma palavra: ')
print embaralhaPalavra(palavra)
