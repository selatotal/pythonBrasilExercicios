letras = []
vogais = ['A', 'E', 'I', 'O', 'U']

for i in range(0, 10):
    letras.append(raw_input('Informe um caracter: ').upper())

totConsoantes = 0
consoantes = []
for i in range(0, 10):
    if letras[i] not in vogais:
        consoantes.append(letras[i])
        totConsoantes += 1

print 'Voce digitou %d consoantes' % totConsoantes
print consoantes
