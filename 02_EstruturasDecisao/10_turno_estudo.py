print 'Informe o turno em que voce estuda'
print '[M]atutino'
print '[V]espertino'
print '[N]oturno'
turno = raw_input('Opcao escolhida: ').upper()

if (turno == 'M'):
    print 'Bom dia!'
elif (turno == 'V'):
    print 'Boa tarde!'
elif (turno == 'N'):
    print 'Boa noite!'
else:
    print 'Valor invalido'
