num1 = int(raw_input('Informe um numero: '))
num2 = int(raw_input('Informe outro numero: '))

if (num1 > num2):
    print num1, 'eh maior que', num2
elif (num1 < num2):
    print num2, 'eh maior que', num1
else:
    print 'Os numeros sao iguais'
