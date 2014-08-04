quantidade = 0
while (quantidade <= 0):
    quantidade = int(raw_input('Informe a quantidade de temperaturas: '))
    if (quantidade <= 0):
        print 'A quandidade deve ser positiva!'

soma = 0.0
for i in range(0, quantidade):
    temperatura = float(raw_input('Informe a temperatura: '))
    if ('maior' not in vars()) or (temperatura > maior):
        maior = temperatura
    if ('menor' not in vars()) or (temperatura < menor):
        menor = temperatura
    soma += temperatura

media = soma / float(quantidade)

print 'Media da temperatura: ', media
print 'Maior temperatura: ', maior
print 'Menor temperatura: ', menor
