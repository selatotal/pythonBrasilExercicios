#!/usr/bin/env python
# _*_ coding: utf-8

letras = {
    'A': '4',
    'E': '3',
    'I': '1',
    'O': '0'
}

senhaInicial = raw_input('Informe a senha original: ')
senhaFinal = ''
maiuscula = True

for caracter in senhaInicial:
    if caracter.upper() in letras.keys():
        senhaFinal += letras[caracter.upper()]
    else:
        if caracter.isalpha():
            if maiuscula:
                senhaFinal += caracter.upper()
            else:
                senhaFinal += caracter.lower()
        else:
            senhaFinal += caracter
    maiuscula = not maiuscula

print senhaFinal
