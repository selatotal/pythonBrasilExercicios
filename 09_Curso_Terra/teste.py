def bolder(func):

	def bolder_func(valor):
		return '<b>' + func(valor) + '</b>'
	
	return bolder_func

@bolder
def ola(string):
	return 'Ola! ' + string

print ola('Jonathan')