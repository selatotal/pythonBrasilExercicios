# -*- coding: utf-8 -*-


def log(msg):
    with open('/tmp/facterutils.log', 'a') as arquivo:
        arquivo.write(msg + '\n')
        arquivo.close()
    return
