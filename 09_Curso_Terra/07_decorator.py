#!/usr/bin/env python
# _*_ coding: utf-8


def jsonToString(func):

    def jsonToString_func():
        dicionario = func()
        retorno = '{\n'
        for chave in dicionario:
            retorno += '\t%s : %s\n' % (chave, dicionario[chave])
        retorno += '}'
        return retorno
    return jsonToString_func


@jsonToString
def retornaDicionario():
    times = {
        'Gremio': 'Felipao',
        'internacional': 'Abel Braga'
    }
    return times

print retornaDicionario()
