peso = float(raw_input('Informe o peso dos peixes pescados:'))
multaPorQuilo = 4.0
pesoMaximo = 50.0

if (peso > pesoMaximo):
    excesso = peso - pesoMaximo
    print 'Excesso de peso:', excesso
    print 'Valor da multa por excesso', excesso * multaPorQuilo
else:
    print 'Nao houve excesso de peso'
