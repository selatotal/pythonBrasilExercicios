#!/usr/bin/env python
# _*_ coding: utf-8


def calcular(*args, **kwargs):

    if (len(args) != 2) or (len(kwargs) != 1):
        print 'Argumentos invalidos'
        return False

    if ('op' not in kwargs.keys()):
        print 'Operacao nao definida'
        return False

    operacao = kwargs['op']
    if (operacao == 'soma'):
        return args[0] + args[1]
    elif (operacao == 'subtracao'):
        return args[0] - args[1]
    elif (operacao == 'multiplicacao'):
        return args[0] * args[1]
    elif (operacao == 'divisao'):
        if (args[1] == 0):
            print 'Divisao por zero'
            return False
        return args[0] / args[1]
    else:
        print 'Operacao invalida'
        return False


print calcular(1, 2, op='soma')
