nota1 = float(raw_input('Informe a primeira nota: '))
nota2 = float(raw_input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2.0

print 'A media do aluno eh:', media
if (media == 10):
    print 'Aprovado com Distincao'
elif (media >= 7):
    print 'Aprovado'
else:
    print 'Reprovado'
