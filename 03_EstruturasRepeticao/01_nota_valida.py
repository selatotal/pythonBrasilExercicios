nota = -1
while (nota < 0) or (nota > 10):
    nota = int(raw_input('Informe uma nota: '))
    if (nota < 0) or (nota > 10):
        print 'Nota Invalida'
