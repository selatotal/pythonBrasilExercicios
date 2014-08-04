continua = 'S'
totalAlunos = 0
somaAcertos = 0

while (continua.upper() == 'S'):
    acertos = 0
    print 'Informe a resposta de cada questao:'
    resposta = raw_input('Questao 1: ').upper()
    if (resposta == 'A'):
        acertos += 1
    resposta = raw_input('Questao 2: ').upper()
    if (resposta == 'B'):
        acertos += 1
    resposta = raw_input('Questao 3: ').upper()
    if (resposta == 'C'):
        acertos += 1
    resposta = raw_input('Questao 4: ').upper()
    if (resposta == 'D'):
        acertos += 1
    resposta = raw_input('Questao 5: ').upper()
    if (resposta == 'E'):
        acertos += 1
    resposta = raw_input('Questao 6: ').upper()
    if (resposta == 'E'):
        acertos += 1
    resposta = raw_input('Questao 7: ').upper()
    if (resposta == 'D'):
        acertos += 1
    resposta = raw_input('Questao 8: ').upper()
    if (resposta == 'C'):
        acertos += 1
    resposta = raw_input('Questao 9: ').upper()
    if (resposta == 'B'):
        acertos += 1
    resposta = raw_input('Questao 10: ').upper()
    if (resposta == 'A'):
        acertos += 1

    somaAcertos += acertos
    print 'Total de Acertos: %d' % acertos

    if ('maiorAcerto' not in vars()) or (acertos > maiorAcerto):
        maiorAcerto = acertos
    if ('menorAcerto' not in vars()) or (acertos < menorAcerto):
        menorAcerto = acertos

    totalAlunos += 1

    continua = raw_input('Deseja continuar (S/N): ').upper()

print 'Maior acerto: %d' % maiorAcerto
print 'Menor acerto: %d' % menorAcerto
print 'Total de alunos que utilizaram o sistema: %d' % totalAlunos
print 'Media de acertos: %.2f' % (somaAcertos / float(totalAlunos))
