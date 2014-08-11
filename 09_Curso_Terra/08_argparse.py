#!/usr/bin/env python
# _*_ coding: utf-8

import argparse

parser = argparse.ArgumentParser(description='Calculadora Simples')
parser.add_argument('--numero1', help='Primeiro Número', type=int, required=True)
parser.add_argument('--numero2', help='Segundo Número', type=int, required=True)
parser.add_argument('--operador', help='Operação', choices=['soma', 'subtracao', 'multiplicacao', 'divisao'], required=True)

argumentos = parser.parse_args()

if (argumentos.operador == 'soma'):
    print argumentos.numero1 + argumentos.numero2
elif (argumentos.operador == 'subtracao'):
    print argumentos.numero1 - argumentos.numero2
elif (argumentos.operador == 'multiplicacao'):
    print argumentos.numero1 * argumentos.numero2
elif (argumentos.operador == 'divisao'):
    if (argumentos.numero2 == 0):
        print 'Erro: Divisao por Zero'
    else:
        print argumentos.numero1 / float(argumentos.numero2)
else:
    print 'Operacao invalida'
