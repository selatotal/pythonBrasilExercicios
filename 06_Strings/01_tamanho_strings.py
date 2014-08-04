print 'Compara duas strings'
string1 = raw_input('String 1: ')
string2 = raw_input('String 2: ')

print 'Tamanho de "%s": %d caracteres' % (string1, len(string1))
print 'Tamanho de "%s": %d caracteres' % (string2, len(string2))

if (len(string1) != len(string2)):
    print 'As duas strings sao de tamanhos diferentes'
    print 'As duas strings possuem conteudo diferente'
else:
    print 'As duas strings tem tamanho igual'
    if (string1 == string2):
        print 'As duas strings possuem o mesmo conteudo'
    else:
        print 'As duas strings possuem conteudo diferente'
