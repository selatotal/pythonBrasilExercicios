data = raw_input('Informe uma data no formato dd/mm/yyyy: ')

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

print dia, mes, ano

bissexto = False
if (ano % 4 == 0):
    bissexto = True
    if (ano % 100 == 0) and (ano % 400 != 0):
        bissexto = False

valida = True
if (mes in (1, 3, 5, 7, 8, 10, 12)):
    if (dia < 1) or (dia > 31):
        valida = False
elif (mes in (4, 6, 9, 11)):
    if (dia < 1) or (dia > 30):
        valida = False
else:
    if (bissexto):
        if (dia < 1) or (dia > 29):
            valida = False
    else:
        if (dia < 1) or (dia > 28):
            valida = False

if (valida):
    print 'Data VALIDA'
else:
    print 'Data INVALIDA'
