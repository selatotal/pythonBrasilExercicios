# Entrada de dados
totalMorangos =\
    float(raw_input('Informe a quantidade (em Kg) de morangos comprados: '))
totalMacas =\
    float(raw_input('Informe a quantidade (em Kg) de macas comprados: '))

# Calcula o valor bruto
if (totalMorangos <= 5):
    valorMorangos = totalMorangos * 2.5
else:
    valorMorangos = totalMorangos * 2.2

if (totalMacas <= 5):
    valorMacas = totalMacas * 1.8
else:
    valorMacas = totalMacas * 1.5

valorBruto = valorMorangos + valorMacas

# Verifica os descontos
if ((totalMorangos + totalMacas) >= 8) or (valorBruto >= 25):
    valorBruto = valorBruto * 0.9

# Imprime o resultado
print 'Valor a pagar: ', valorBruto
