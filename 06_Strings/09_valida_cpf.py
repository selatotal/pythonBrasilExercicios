def validaCPF(cpf):

    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if (len(cpf) != 11):
        return False

    # Realiza a multiplicacao dos 9 primeiros numeros
    fator = 10
    soma = 0
    for i in range(0, 9):
        soma += (int(cpf[i]) * fator)
        fator -= 1

    # Divide o somatorio por 11 e pega o resto
    resto = soma % 11

    # Se o resto eh menor que 2, entao o primeiro digito verificador eh 0,
    #  senao diminui o resto do valor 11
    if (resto < 2):
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Agora verifica o segundo digito com os 10 primeiros numeros
    fator = 11
    soma = 0
    for i in range(0, 10):
        soma += (int(cpf[i]) * fator)
        fator -= 1

    # Divide o somatorio por 11 e pega o resto
    resto = soma % 11

    # Se o resto eh menor que 2, entao o segundo digito verificador eh 0,
    #  senao diminui o resto do valor 11
    if (resto < 2):
        digito2 = 0
    else:
        digito2 = 11 - resto

    if (int(cpf[9]) == digito1) and (int(cpf[10]) == digito2):
        return True

    return False

###
# FLUXO PRINCIPAL

cpf = raw_input('Informe o CPF: ')
if (validaCPF(cpf)):
    print 'CPF valido'
else:
    print 'CPF INVALIDO'
