populacaoA = 0
crescimentoA = 0

# Solicita ao usuario o valor das populacoes e taxas de crescimento
while (populacaoA <= 0):
    populacaoA = int(raw_input('Informe a populacao do pais A: '))
    if (populacaoA <= 0):
        print 'Populacao deve ser um valor positivo'
while (crescimentoA <= 0):
    crescimentoA = float(
        raw_input('Informe o percentual de crescimento do pais A: '))
    if (crescimentoA <= 0):
        print 'Percentual de crescimento deve ser um valor positivo'
populacaoB = populacaoA
while (populacaoB <= populacaoA):
    populacaoB = int(raw_input('Informe a populacao do pais B: '))
    if (populacaoB <= populacaoA):
        print 'Populacao do pais B deve ser maior que a populacao do pais A'
crescimentoB = crescimentoA
while (crescimentoB >= crescimentoA):
    crescimentoB = float(
        raw_input('Informe o percentual de crescimento do pais B: '))
    if (crescimentoB >= crescimentoA):
        print 'Percentual de crescimento do pais B deve ser menor que o do '\
            'pais A'

crescimentoA = 1 + (crescimentoA / 100.0)
crescimentoB = 1 + (crescimentoB / 100.0)

# Realiza calculo de anos
ano = 1
while (populacaoA <= populacaoB):
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    ano += 1

# Imprime o resultado
print 'Serao necessarios', ano, 'anos para que a populacao do pais A '\
    'ultrapasse a populacao do pais B'
