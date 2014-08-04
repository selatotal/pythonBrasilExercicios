import re


def validaData(dia, mes, ano):
    # Valida o dia
    if (dia < 0) or (dia > 31):
        return False

    # Valida mes com 30 dias
    meses30 = (4, 6, 9, 11)
    if (mes in meses30):
        if (dia > 30):
            return False

    # Valida fevereiro e anos bissextos
    if (mes == 2):
        if (dia > 28):
            if (ano % 4 != 0):
                return False
            elif (ano % 100 == 0) and (ano % 1000 != 0):
                return False

    return True


def dataPorExtenso(data):
    # Valida o formato da data por expressao regular
    reg = re.compile('^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$')
    if (not (reg.match(data))):
        print 'Data invalida'
        return None

    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if (not validaData(dia, mes, ano)):
        return None

    mesExtenso = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
                  'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
                  'Dezembro')

    return '%d de %s de %d' % (dia, mesExtenso[mes - 1], ano)

# Fluxo Principal

data = raw_input('Informe uma data no formato dd/mm/yyyy: ')
print dataPorExtenso(data)
