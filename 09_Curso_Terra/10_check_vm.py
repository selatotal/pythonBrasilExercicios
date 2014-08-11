#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

process = Popen('facter', stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

if 'is_virtual => true' in stdout:
    print 'Estou em uma maquina virtual'
else:
    print 'Estou em uma maquina real'
