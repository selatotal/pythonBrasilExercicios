#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import argparse

# Realiza o parse dos argumentos
parser = argparse.ArgumentParser(description='Facter Viewer')
parser.add_argument('-v', help='Valor a ser buscado', type=str, required=True)

argumentos = parser.parse_args()

# Busca a lista de argumentos e coloca em um dictionary
process = Popen('facter', stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

dicionario = {}
for line in stdout.split('\n'):
    if len(line) > 0:
        entrada = line.split(' => ', 2)
        dicionario[entrada[0]] = entrada[1]

# Imprime o valor desejado ou todos
if (argumentos.v == 'all'):
    for chave in sorted(dicionario):
        print '%s : %s' % (chave, dicionario[chave])
else:
    if (argumentos.v in dicionario.keys()):
        print '%s : %s' % (argumentos.v, dicionario[argumentos.v])
    else:
        print 'Valor nao encontrado'
