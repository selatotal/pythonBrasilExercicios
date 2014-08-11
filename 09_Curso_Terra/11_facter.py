#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

process = Popen('facter', stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

dicionario = {}
for line in stdout.split('\n'):
    if len(line) > 0:
        entrada = line.split(' => ', 2)
        dicionario[entrada[0]] = entrada[1]

print dicionario
