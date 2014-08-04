quantidade = 0
while (quantidade <= 0):
    quantidade = int(raw_input('Voce quer saber a media de quantas notas: '))
    if (quantidade <= 0):
        print 'A quandidade deve ser positiva!'

soma = 0.0
for i in range(0, quantidade):
    nota = -1
    while (nota < 0) or (nota > 10):
        nota = float(raw_input('Informe a nota: '))
        if (nota < 0) or (nota > 10):
            print 'A nota deve estar entre 0 e 10'
    soma += nota

print 'A media das notas eh', (soma / float(quantidade))
