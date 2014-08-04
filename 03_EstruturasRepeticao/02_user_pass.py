usuario = senha = ''
while (usuario == senha):
    usuario = raw_input('Informe um nome de usuario: ')
    senha = raw_input('Informe a senha: ')
    if (usuario == senha):
        print 'A senha nao pode ser igual ao nome do usuario'
