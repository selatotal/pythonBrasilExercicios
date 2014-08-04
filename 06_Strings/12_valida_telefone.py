print 'Valida e corrige numero de telefone'
telefone = raw_input('Telefone: ')

telefoneLimpo = telefone.replace('-', '')

if (len(telefoneLimpo) == 7):
    print 'Telefone possui 7 digitos. Vou acrescentar o digito tres na frente.'
    print 'Telefone corrigido sem formatacao: 3%s' % telefoneLimpo
    print 'Telefone corrigido com formatacao: 3%s' % telefone
