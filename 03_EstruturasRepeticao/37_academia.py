codigo = -1
totalClientes = 0
somaAlturas = 0.0
somaPesos = 0.0
while (codigo != 0):
    codigo = int(raw_input('Informe o codigo do cliente: '))
    if (codigo != 0):
        altura = float(raw_input('Informe a altura do cliente: '))
        peso = float(raw_input('Informe o peso do cliente:'))
        totalClientes += 1
        somaAlturas += altura
        somaPesos += peso
        if ('maisAlto' not in vars()) or (altura > maisAlto):
            maisAlto = altura
            codigoMaisAlto = codigo
        if ('maisBaixo' not in vars()) or (altura < maisBaixo):
            maisBaixo = altura
            codigoMaisBaixo = codigo
        if ('maisGordo' not in vars()) or (peso > maisGordo):
            maisGordo = peso
            codigoMaisGordo = codigo
        if ('maisMagro' not in vars()) or (peso < maisMagro):
            maisMagro = peso
            codigoMaisMagro = codigo

print 'O cliente mais alto eh o de codigo %i com %f' %\
    (codigoMaisAlto, maisAlto)
print 'O cliente mais baixo eh o de codigo %i com %f' %\
    (codigoMaisBaixo, maisBaixo)
print 'O cliente mais magro eh o de codigo %i com %f' %\
    (codigoMaisMagro, maisMagro)
print 'O cliente mais gordo eh o de codigo %i com %f' %\
    (codigoMaisGordo, maisGordo)

print 'Media da altura dos clientes: %.2f' %\
    (somaAlturas / float(totalClientes))
print 'Media dos pesos dos clientes: %.2f' %\
    (somaPesos / float(totalClientes))
