nota1 = float(raw_input('Informe o valor da primeira nota: '))
nota2 = float(raw_input('Informe o valor da segunda nota: '))

media = (nota1 + nota2) / 2

if (media < 4):
    print 'Conceito: E'
    aprovado = False
elif (media < 6):
    print 'Conceito: D'
    aprovado = False
elif (media < 7.5):
    print 'Conceito: C'
    aprovado = True
elif (media < 9):
    print 'Conceito: B'
    aprovado = True
else:
    print 'Conceito: A'
    aprovado = True

if (aprovado):
    print 'APROVADO'
else:
    print 'REPROVADO'
