letra = raw_input('Informe uma letra: ')

if ('AEIOU'.find(letra.upper()) >= 0):
    print 'VOGAL'
else:
    print 'CONSOANTE'
