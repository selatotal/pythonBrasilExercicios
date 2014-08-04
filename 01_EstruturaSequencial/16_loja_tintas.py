tamanho = float(raw_input('Quantos metros quadrados devem ser pintados: '))

litros = tamanho / 3.0
latas = int(litros / 18.0)
if (litros % 18 != 0):
    latas += 1

print 'Voce devera comprar', latas, 'latas.'
print 'O valor total eh:', latas * 80
