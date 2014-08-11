#!/usr/bin/env python
# _*_ coding: utf-8

from IPy import IP

userNetwork = raw_input('Informe um IP ou uma rede: ')

network = IP(userNetwork)

for ip in network:
    print ip
