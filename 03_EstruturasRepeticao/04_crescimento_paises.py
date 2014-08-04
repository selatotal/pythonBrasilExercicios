# Define os valores de populacao e crescimento
populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015

# Realiza calculo de anos
ano = 1
while (populacaoA <= populacaoB):
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    ano += 1

# Imprime o resultado
print 'Serao necessarios', ano, 'anos para que a populacao do pais A'\
    ' ultrapasse a populacao do pais B'
