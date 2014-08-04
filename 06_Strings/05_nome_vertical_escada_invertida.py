nome = raw_input('Informe seu nome: ')
for i in range(len(nome) - 1, -1, -1):
    for j in range(0, i + 1):
        print nome[j],
    print
