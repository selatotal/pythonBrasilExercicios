# Exercícios do Curso do Terra

## Material do Curso
Disponível em [TreinamentoPythonTerra.pdf](TreinamentoPythonTerra.pdf?raw=true)

## Desafio 1
* 20 + 5 * 4 + 2 deve dar 150. O que falta para isso?

## Desafio 2

* 1 Euro = 1.35 dólares.
* Quanto é 65.54 dólares em Euros?

## Desafio 3

Fazer um script que pergunte o nome do servidor.
Validar de o servidor pertence ao terra checando se estão nos domínios terra.* ou trrsf.*
Escrever na tela se o servidor faz parte de MIA, POA ou CIS. Senão, devolver "Datacenter desconhecido".

## Desafio 4
Escrever um dicionário onde a chave é o nome da equipe no Terra ou produto principal em que trabalha e o valor é uma lista de tuplas onde cada item é o nome de cada colega de equipe e o RE (fake).
Listar esses dados

## Desafio 5
	from IPy import IP
	network = IP ('192.168.0.0/30')
	for ip in network:
		print ip
Continuando o programa acima, adicionar uma verificação que, se o usuário digitar uma rede, ele deve escrever os IPS dessa rede.

## Desafio 6
	def func(*args, **kwargs):
		print kwargs (dict dos argumentos nomeados)
		print args (dict dos argumentos posicionais)
Criar um programa para calculadora de modo que ele possua  apenas uma função chamada calcular como no exemplo abaixo, utilizando funções com args/kwargs:

	calcular(1, 2, op='soma')

## Desafio 7
	def bolder(func):
	
		def bolder_func(valor):
			return '<b>' + func(valor) + '</b>'
		
		return bolder_func
	
	@bolder
	def ola(string):
		return 'Ola! ' + string
	
	print ola('Jonathan')

* Criar uma função que retorne um dicionário de chave e valor como um String
* Criar um decorator que transforme este dicionário em JSON como String
* Sem libs externas

## Desafio 8
Usando o argparse, fazer um programa que receba n1, op e n2 como parâmetros.
Exemplo:

	python calc.py --numero1 1 --numero2 2 --operador soma
	>> 3

## Desafio 9
Criar um gerador de senhas, onde o usuário digita 'terra' e a saída seja 'T3Rr4'

## Desafio 10
Usando o Popen com facter e o atributo 'is_virtual => true/false', descobrir se a máquina é virtual ou não.

	$ python check_vm.py
	>>> É uma máquina virtual

## Desafio 11
Usando o Popen com facter, a função split, colocar os dados do facter em um dicionário.

	$ python facter.py
	>>> { 'interfaces' : 'eth0,lo' } (...)

## Desafio 12
Utilizando tudo o que foi visto anteriormente, criar um script que receba o valor que o facter precisa buscar. Se o valor for 'all', então retorna todos.

	$ python facter.py -v swapfree
	>> 1.89 GB
	$ python facter.py -v all
	>> architecture = i386
	>> domain = corp.terra
	...

## Desafio 13
Facter + Log
Adicionar logs ao script facter.py
Deve ser feita uma função def log(msg) no módulo facterutils
Deve usar _with_

## Desafio 14
* Abrir o arquivo names.csv usando open()
* Cada linha representa uma lista separada por ponto-e-vírgula. Colocar os nomes em conjuntos (sets)
* Verificar quais nomes do conjunto 1 aparecem no conjunto 2, porém que não estejam no conjunto 3

## Desafio 15
	class NumeroRomano():
	
		def __init__(self, numero):
			self.mapa = { 'V' : 5, 'X' : 10 }
			self.numero = self.mapa[numero]
			self.romano = numero
		
		def get(self):
			return self.numero
	
	num1 = NumeroRomano('X')  # 10
	num2 = NumeroRomano('V')  # 5
	
	print num1 > num2   # 5 é maior que 10?

Permitir que a classe acima seja utilizada em:

	print int(num1)
	>> 10
	print str(num1)
	>> X

## Desafio 16
Criar uma aplicação flask que receba um campo do factor como parâmetro e retorne seu respectivo valor.
É necessário utilizar a estrutura de templates do flask