tamanho = float(raw_input('Quantos metros quadrados devem ser pintados: '))

litros = (tamanho / 6.0) * 1.1  # 10% de folga
latas = int(litros / 18.0)
galoes = int(litros / 3.6)

# Calculo de latas
if (litros % 18 != 0):
    latas += 1

# Calculo de galoes
if (litros % 3.6 != 0):
    galoes += 1

# Calculo misturando latas e galoes
mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1

print 'Latas:', latas, '. Valor:', latas * 80
print 'Galoes:', galoes, '. Valor:', galoes * 25
print 'Latas:', mixLatas, 'e', mixGaloes, '. Valor: ', \
    (mixLatas * 80)+(mixGaloes*25)
