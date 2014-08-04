def somaImposto(taxaImposto, custo):
    custo = custo + (custo * taxaImposto / 100.0)
    return custo

taxa = float(raw_input('Informe o valor da taxa de imposto: '))
custo = float(raw_input('Informe o custo do produto: '))

custo = somaImposto(taxa, custo)

print 'O preco com impostos eh: %.2f' % custo
