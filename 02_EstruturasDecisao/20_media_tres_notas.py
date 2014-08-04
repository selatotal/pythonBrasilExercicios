nota1 = float(raw_input('Informe a primeira nota: '))
nota2 = float(raw_input('Informe a segunda nota: '))
nota3 = float(raw_input('Informe a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3.0

print 'Media do aluno: {}'.format(media)
if (media == 10):
    print 'Aprovado com Distincao'
elif (media >= 7):
    print 'Aprovado'
else:
    print 'Reprovado'
