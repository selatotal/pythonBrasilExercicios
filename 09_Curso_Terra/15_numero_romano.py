#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NumeroRomano():

    def __init__(self, numero):
        self.mapa = {'V': 5, 'X': 10}
        self.numero = self.mapa[numero]
        self.romano = numero

    def get(self):
        return self.numero

    def __trunc__(self):
        return self.numero

    def __str__(self):
        return self.romano

num1 = NumeroRomano('X')  # 10
num2 = NumeroRomano('V')  # 5

print int(num1)
print int(num2)
print num1
print num2

print num1 > num2  # 10 é maior que 5?
print int(num1) > int(num2)  # 10 é maior que 5?
