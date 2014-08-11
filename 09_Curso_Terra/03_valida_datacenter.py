#!/usr/bin/env python
# _*_ coding: utf-8

servidor = raw_input('Informe o nome do servidor: ')

if ('terra.' in servidor) or ('trrsf.' in servidor):
    print 'Servidor pertence ao Terra'
    if 'poa' in servidor:
        print 'Datacenter: POA'
    elif 'mia' in servidor:
        print 'Datacenter: MIA'
    elif 'cis' in servidor:
        print 'Datacenter: CIS'
    else:
        print 'Datacenter desconhecido'
else:
    print 'Servidor não pertence ao Terra'
