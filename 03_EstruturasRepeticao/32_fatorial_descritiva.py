termo = 0
while (termo <= 0):
    termo = int(raw_input('Voce quer o fatorial de qual termo: '))
    if (termo <= 0):
        print 'O termo deve ser positivo!'

fatorial = 1
print 'Fatorial de ' % termo,
print '!%d = ' % termo,
for i in reversed(range(2, termo + 1)):
    print '%d * ' % i,
    fatorial *= i

print '1 = %d' % fatorial
