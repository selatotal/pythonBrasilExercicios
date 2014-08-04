somaVeiculos = 0
somaAcidentes = 0
somaAcidentesMenos2Mil = 0
totalCidadesMenos2Mil = 0

for i in range(0, 5):
    codigo = int(raw_input('Informe o codigo da cidade: '))
    veiculos = int(raw_input('Informe o numero de veiculos de passeio: '))
    acidentes = int(raw_input('Informe a quantidade de acidentes em 1999: '))

    indiceAcidentes = acidentes / float(veiculos)
    somaVeiculos += veiculos

    if ('maisAcidentes' not in vars()) or (indiceAcidentes > maisAcidentes):
        maisAcidentes = indiceAcidentes
        codigoMaisAcidentes = codigo
    if ('menosAcidentes' not in vars()) or (indiceAcidentes < menosAcidentes):
        menosAcidentes = indiceAcidentes
        codigoMenosAcidentes = codigo

    if (veiculos < 2000):
        somaAcidentesMenos2Mil += acidentes
        totalCidadesMenos2Mil += 1

print 'O cidade com maior indice de acidentes eh %i com %.2f' %\
    (codigoMaisAcidentes, maisAcidentes)
print 'O cidade com menor indice de acidentes eh %i com %.2f' %\
    (codigoMenosAcidentes, menosAcidentes)
print 'A media de veiculos nas cidades eh %.2f' % (somaVeiculos / 5.0)
print 'A media de acidentes de transito nas cidades com menos '\
    'de 2k veiculos eh %.2f' %\
    (somaAcidentesMenos2Mil / float(totalCidadesMenos2Mil))
