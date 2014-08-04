num1 = int(raw_input('Informe um numero: '))
num2 = int(raw_input('Informe outro numero: '))
num3 = int(raw_input('Informe mais um numero: '))

if (num1 >= num2) and (num1 >= num3):
    print num1
    if (num2 >= num3):
        print num2
        print num3
    else:
        print num3
        print num2
elif (num2 >= num3):
    print num2
    if (num1 >= num3):
        print num1
        print num3
    else:
        print num3
        print num1
else:
    print num3
    if (num1 >= num2):
        print num1
        print num2
    else:
        print num2
        print num1
