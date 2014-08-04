def validaIP(ipAddress):
    blocos = ipAddress.split('.')
    if (len(blocos) != 4):
        return False
    for i in blocos:
        i_i = int(i)
        if (i_i < 0) or (i_i > 255):
            return False
    return True

# FLUXO PRINCIPAL
arquivoEntrada = open('01_entrada.txt', 'r')
linhas = arquivoEntrada.readlines()
arquivoEntrada.close()

ipsValidos = []
ipsInvalidos = []

for ip in linhas:
    if (validaIP(ip.strip())):
        ipsValidos.append(ip.strip())
    else:
        ipsInvalidos.append(ip.strip())

arquivoSaida = open('01_saida.txt', 'w')

arquivoSaida.write('[IPs Validos]\n')
for ip in ipsValidos:
    arquivoSaida.write('%s\n' % ip)

arquivoSaida.write('\n[IPs Invalidos]\n')
for ip in ipsInvalidos:
    arquivoSaida.write('%s\n' % ip)

arquivoSaida.close()
