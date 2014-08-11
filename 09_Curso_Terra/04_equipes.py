#!/usr/bin/env python
# _*_ coding: utf-8

equipes = {
    'tecnologiaportal': (
        ('tales', '01'),
        ('gustavo', '02'),
        ('robson', '03')
    ),
    'tecnologiavideos': (
        ('cunha', '04'),
        ('broto', '05')
    )
}

for equipe in equipes:
    print 'Equipe: %s' % equipe
    for funcionario in equipes[equipe]:
        print '\tNome: %s\tRE: %s' % (funcionario)
