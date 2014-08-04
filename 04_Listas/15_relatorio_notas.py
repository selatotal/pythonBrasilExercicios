valores = []
valor = 0

while (valor != -1):
    valor = int(raw_input('Informe um valor: '))
    if (valor != -1):
        valores.append(valor)

print 'Quantidade de valores lidos: %d' % len(valores)
print valores
valores.reverse()
print valores

somaValores = 0
for valor in valores:
    somaValores += valor

media = somaValores / float(len(valores))
print 'Soma dos Valores: %d' % somaValores
print 'Media dos Valores: %.2f' % media

valoresAcimaDaMedia = 0
valoresAcimaDeSete = 0
for valor in valores:
    if (valor >= media):
        valoresAcimaDaMedia += 1
    if (valor >= 7):
        valoresAcimaDeSete += 1

print 'Valores acima da media: %d' % valoresAcimaDaMedia
print 'Valores acima de sete: %d' % valoresAcimaDeSete
