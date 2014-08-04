string = raw_input('Informe uma string: ')

espacos = 0
vogais = 0
for i in string:
    if ('AEIOU'.find(i.upper()) >= 0):
        vogais += 1
    elif (i == ' '):
        espacos += 1

print '%d espacos e %d vogais' % (espacos, vogais)
