print 'Informe os valores dos lados do triangulo'
lado1 = float(raw_input('Lado 1: '))
lado2 = float(raw_input('Lado 2: '))
lado3 = float(raw_input('Lado 3: '))

# Verifica se eh um triangulo
if (lado1 > (lado2 + lado3)) or (lado2 > (lado1 + lado3))\
        or (lado3 > (lado1 + lado2)):
    ehTriangulo = False
else:
    ehTriangulo = True

if (ehTriangulo):
    print 'Os valores formam um Triangulo'
    # Verifica o tipo de triangulo
    if (lado1 == lado2) and (lado2 == lado3):
        print 'Triangulo Equilatero'
    elif (lado1 == lado2) or (lado1 == lado2) or (lado2 == lado3):
        print 'Triangulo Isosceles'
    else:
        print 'Triangulo Escaleno'
else:
    print 'Os valores nao formam um Triangulo'
