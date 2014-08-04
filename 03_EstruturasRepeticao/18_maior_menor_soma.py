quantidade = 0
while (quantidade <= 0):
    quantidade = int(raw_input('Voce quer informar quantos numeros: '))
    if (quantidade <= 0):
        print 'Quantidade deve ser positiva!'

soma = 0
for i in range(0, quantidade):
    numero = int(raw_input('Informe um numero: '))
    if ('maior' not in vars()) or (numero > maior):
        maior = numero

    if ('menor' not in vars()) or (numero < menor):
        menor = numero

    soma += numero

print 'Menor numero:', menor
print 'Maior numero:', maior
print 'Soma dos numeros:', soma
