ano = int(raw_input('Informe um ano: '))

bissexto = False
if (ano % 4 == 0):
    bissexto = True
    if (ano % 100 == 0) and (ano % 400 != 0):
        bissexto = False

if (bissexto):
    print 'O ano eh BISSEXTO'
else:
    print 'O ano NAO EH BISSEXTO'
