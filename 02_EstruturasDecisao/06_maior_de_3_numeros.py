num1 = int(raw_input('Informe um numero: '))
num2 = int(raw_input('Informe outro numero: '))
num3 = int(raw_input('Informe mais um numero: '))

if (num1 == num2) and (num1 == num3):
    print 'Os numeros sao iguais'
elif (num1 > num2) and (num1 > num3):
    print 'O maior numero eh:', num1
elif (num2 > num3):
    print 'O maior numero eh:', num2
else:
    print 'O maior numero eh:', num3
