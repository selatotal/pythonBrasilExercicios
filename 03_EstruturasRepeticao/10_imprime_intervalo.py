inicial = int(raw_input('Informe o valor inicial: '))
final = inicial
while (final <= inicial):
    final = int(raw_input('Informe o valor final: '))
    if (final <= inicial):
        print 'O valor final deve ser maior que o valor final!'

for i in range(inicial, final + 1):
    print i
