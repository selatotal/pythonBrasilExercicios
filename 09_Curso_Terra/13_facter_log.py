#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
from facterutils import log
import argparse

# Realiza o parse dos argumentos
parser = argparse.ArgumentParser(description='Facter Viewer')
parser.add_argument('-v', help='Valor a ser buscado', type=str, required=True)

argumentos = parser.parse_args()

# Busca a lista de argumentos e coloca em um dictionary
process = Popen('facter', stdout=PIPE, stderr=PIPE)
log('Executando facter')
stdout, stderr = process.communicate()

log('Criando dicionario')
dicionario = {}
for line in stdout.split('\n'):
    if len(line) > 0:
        entrada = line.split(' => ', 2)
        dicionario[entrada[0]] = entrada[1]

# Imprime o valor desejado ou todos
if (argumentos.v == 'all'):
    log('Selecionando todos os argumentos')
    for chave in sorted(dicionario):
        print '%s : %s' % (chave, dicionario[chave])
else:
    log('Procurando argumento informado')
    if (argumentos.v in dicionario.keys()):
        print '%s : %s' % (argumentos.v, dicionario[argumentos.v])
    else:
        log('Valor nao encontrado')
        print 'Valor nao encontrado'
