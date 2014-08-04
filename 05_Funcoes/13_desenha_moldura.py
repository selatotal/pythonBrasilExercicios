def desenhaMoldura(linhas=1, colunas=1):
    if (linhas < 1):
        linhas = 1
    elif (linhas > 20):
        linhas = 20

    if (colunas < 1):
        colunas = 1
    elif (colunas > 20):
        colunas = 20

    for i in range(0, linhas):
        if (i == 0) or (i == (linhas - 1)):
            print '+',
            for j in range(1, colunas - 1):
                print '-',
            if (colunas > 1):
                print '+'
            else:
                print
        else:
            print '|',
            for j in range(1, colunas - 1):
                print ' ',
            if (colunas > 1):
                print '|'
            else:
                print

# FLUXO PRINCIPAL
linhas = int(raw_input('Informe a quantidade de linhas da moldura: '))
colunas = int(raw_input('Informe a quantidade de colunas da moldura: '))
desenhaMoldura(linhas, colunas)
