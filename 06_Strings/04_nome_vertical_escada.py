nome = raw_input('Informe seu nome: ')
for i in range(0, len(nome)):
    for j in range(0, i + 1):
        print nome[i],
    print
