def verificaPositivo(valor):
    if (valor > 0):
        return 'P'
    else:
        return 'N'

numero = int(raw_input('Informe um numero: '))
print 'Resultado: %s' % verificaPositivo(numero)
