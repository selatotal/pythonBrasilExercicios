# Solicita informacoes
tipoCombustivel =\
    raw_input('Informe (A) para Alcool ou (G) para Gasolina: ').upper()
quantidadeLitros = float(raw_input('Informe a quantidade de litros: '))

# Define o valor e os descontos
if (tipoCombustivel == 'A'):
    valor = 1.9
    if (quantidadeLitros <= 20):
        desconto = 3
    else:
        desconto = 5
else:
    valor = 2.5
    if (quantidadeLitros <= 20):
        desconto = 4
    else:
        desconto = 6

# Calcula o total
totalPagar = (valor * quantidadeLitros) * ((100 - desconto) / 100.0)

print 'Total a pagar: ', totalPagar
