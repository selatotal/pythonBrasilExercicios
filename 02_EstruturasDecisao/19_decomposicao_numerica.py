num = int(raw_input('Informe um numero inteiro: '))

centenas = num / 100
dezenas = (num - (centenas * 100)) / 10
unidades = (num - (centenas * 100) - (dezenas * 10))

saida = ''
if (centenas > 0):
    saida = saida + str(centenas)
    if (centenas > 1):
        saida = saida + ' centenas '
    else:
        saida = saida + ' centena '

if (dezenas > 0):
    if (unidades == 0) and (centenas != 0):
        saida = saida + 'e '
    saida = saida + str(dezenas)
    if (dezenas > 1):
        saida = saida + ' dezenas '
    else:
        saida = saida + ' dezena '

if (unidades > 0):
    if (centenas != 0) or (dezenas != 0):
        saida = saida + 'e '
    saida = saida + str(unidades)
    if (unidades > 1):
        saida = saida + ' unidades'
    else:
        saida = saida + ' unidade'

print saida
