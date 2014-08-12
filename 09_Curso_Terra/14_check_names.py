#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('names.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    arquivo.close()

cont = 1
nomes = {}
for linha in linhas:
    nomes[cont] = linha.split(';')
    cont += 1

for nome in nomes[1]:
    if (nome in nomes[2]) and (nome not in nomes[3]):
        print nome
