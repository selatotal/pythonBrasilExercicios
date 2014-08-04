from Ponto import Ponto
from Retangulo import Retangulo

ponto1 = Ponto(10, 20)
ponto2 = Ponto(30, 40)

ret1 = Retangulo(10, 20, ponto1)
ret2 = Retangulo(30, 40, ponto2)
ret1.mostraCentro()
ret2.mostraCentro()
