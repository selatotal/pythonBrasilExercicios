salarioBase = 200
vendedores = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    valorVendas = float(raw_input('Informe o valor das vendas do vendedor: '))
    salario = valorVendas * 0.09 + salarioBase
    indice = int(salario / 100) - 1
    if (indice > 9):
        indice = 9
    elif (indice < 1):
        indice = 1
    print indice
    vendedores[indice - 1] += 1

for i in range(0, 9):
    print '%d - %d : %d' % (i * 100 + 200, (i + 1) * 100 + 199, vendedores[i])
