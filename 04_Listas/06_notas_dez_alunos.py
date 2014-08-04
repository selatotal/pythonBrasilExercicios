notas = []
for i in range(0, 10):
    notasAluno = []
    for j in range(0, 4):
        notasAluno.append(
            float(raw_input('Informe a nota do aluno %.d: ' % (i + 1))))
    notas.append(notasAluno)

alunosMedia = 0
for notasAluno in notas:
    somaNotas = 0
    for nota in notasAluno:
        somaNotas += nota
    if ((somaNotas / 4.0) >= 7.0):
        alunosMedia += 1

print '%d alunos ficaram acima da media' % alunosMedia
