tamanho = float(raw_input('Informe o tamanho do arquivo (em MB): '))
velocidade = float(raw_input('Informe a velocidade de conexao (em Mbps): '))

tamanhoBits = tamanho * 1024 * 1024 * 8
tempoSegundos = tamanhoBits / (velocidade * 1024 * 1024)
tempoMinutos = tempoSegundos / 60

print 'Tempo aproximado de download:', tempoMinutos, 'minutos'
