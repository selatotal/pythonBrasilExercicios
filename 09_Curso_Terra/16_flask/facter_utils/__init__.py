# -*- coding: utf-8 -*-


from subprocess import Popen, PIPE


def log(msg):
    with open('/tmp/facterutils.log', 'a') as arquivo:
        arquivo.write(msg + '\n')
        arquivo.close()
    return


def get_argument(argumento):
    # Busca a lista de argumentos e coloca em um dictionary
    process = Popen('facter', stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    dicionario = {}
    for line in stdout.split('\n'):
        if len(line) > 0:
            entrada = line.split(' => ', 2)
            dicionario[entrada[0]] = entrada[1]

    # Imprime o valor desejado ou todos
    log('Procurando argumento informado')
    if (argumento in dicionario.keys()):
        return dicionario[argumento]
    else:
        log('Valor nao encontrado')
        return None
