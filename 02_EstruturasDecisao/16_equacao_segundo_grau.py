import math

print 'Calculo de equacao de Segundo Grau'
valorA = float(raw_input('Informe o valor de a : '))
valorB = float(raw_input('Informe o valor de b : '))
valorC = float(raw_input('Informe o valor de c : '))

# Verifica se eh uma equacao de segundo grau
if (valorA == 0):
    print 'Os valores nao formam uma equacao de segundo grau'
else:
    # Calcula o Delta
    delta = math.pow(valorB, 2) - (4 * valorA * valorC)

    if (delta < 0):
        print 'A equacao nao possui valores reais.'
    elif (delta == 0):
        print 'A equacao possui apenas uma raiz'
        raiz = -(valorB) / (2 * valorA)
        print 'Raiz:', raiz
    else:
        print 'A equacao possui duas raizes'
        raiz1 = (-(valorB) + math.sqrt(delta)) / (2 * valorA)
        raiz2 = (-(valorB) - math.sqrt(delta)) / (2 * valorA)
        print 'Raiz 1:', raiz1
        print 'Raiz 2:', raiz2
