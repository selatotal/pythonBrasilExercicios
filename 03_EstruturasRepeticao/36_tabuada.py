tabuada = int(raw_input('Montar a tabuada de: '))

comecar = -1
while (comecar < 0):
    comecar = int(raw_input('Comecar por: '))
    if (comecar < 0):
        print 'O numero deve ser maior que 0'

terminar = comecar
while (comecar >= terminar):
    terminar = int(raw_input('Terminar em: '))
    if (comecar >= terminar):
        print 'Deve terminar com um numero maior que o de comecar'

print 'Vou montar a tabuada de', tabuada, 'comecando em', comecar,\
    'e terminando em', terminar
for i in range(comecar, terminar + 1):
    print '%i X %i = %i' % (tabuada, i, tabuada * i)
