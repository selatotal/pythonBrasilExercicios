# Abre o arquivo para leitura
arquivoEntrada = open('23_entrada.txt', 'r')

# Coloca todas as linhas em memoria
linhas = arquivoEntrada.readlines()

# Fecha o arquivo
arquivoEntrada.close()

usuarios = []
espacosUtilizados = []
espacoTotal = 0.0
for linha in linhas:
    campos = linha.split()
    usuario = campos[0]
    espacoUtilizado = int(campos[1])
    usuarios.append(usuario)
    espacosUtilizados.append(espacoUtilizado)
    espacoTotal += espacoUtilizado

# Abre o arquivo para escrita
arquivoSaida = open('23_saida.txt', 'w')

arquivoSaida.write(
    'ACME Inc.               Uso do espaco em disco pelos usuarios\n')
arquivoSaida.write(
    '------------------------------------------------------------------------')
arquivoSaida.write('\nNr.  Usuario        Espaco utilizado     %% do uso')

for i in range(0, len(usuarios)):
    espacoMB = espacosUtilizados[i] / (1024.0 * 1024.0)
    percentualUso = espacosUtilizados[i] / espacoTotal
    arquivoSaida.write('\n%d - %s - %.2f MB - %.2f%%' %
                       (i + 1, usuarios[i], espacoMB, percentualUso * 100.0))

arquivoSaida.write('\nEspaco total ocupado: %.2f MB' %
                   (espacoTotal / (1024.0 * 1024.0)))
arquivoSaida.write('\nEspaco medio ocupado: %.2f MB' %
                   (espacoTotal / len(usuarios) / (1024.0 * 1024.0)))

# Fecha o arquivo
arquivoSaida.close()
