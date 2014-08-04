quantidade = 0
while (quantidade <= 0):
    quantidade = int(raw_input('Informe a quantidade de turmas: '))
    if (quantidade <= 0):
        print 'A quandidade deve ser positiva!'

soma = 0
for i in range(0, quantidade):
    alunos = -1
    while (alunos < 0) or (alunos > 40):
        alunos = int(raw_input('Informe a quantidade de alunos da turma: '))
        if (alunos < 0) or (alunos > 40):
            print 'A turma deve ter ate 40 alunos'
    soma += alunos

media = soma / float(quantidade)

print 'Media de alunos por turma', media
