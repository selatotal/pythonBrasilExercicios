def quantidadeDigitos(digito):
    if (digito == 0):
        return 0
    return 1 + quantidadeDigitos(digito / 10)

# Fluxo Principal
digito = int(raw_input('Informe um numero inteiro: '))
print 'O numero %d possui %d digitos.' % (digito, quantidadeDigitos(digito))
