string = raw_input('Informe uma string: ').upper()
contrario = string[::-1]

if (string.replace(' ', '') == contrario.replace(' ', '')):
    print 'A string eh um palindromo'
else:
    print 'A string NAO eh um palindromo'
