soma = 0.0
quantidade = 1
precoMercadoria = 1
while (precoMercadoria != 0):
    precoMercadoria = float(raw_input('Produto %d: R$ ' % (quantidade)))
    soma += precoMercadoria

print 'Total: R$ %.2f' % soma
pagamento = float(raw_input('Dinheiro: R$ '))

print 'Troco: R$ %.2f' % (pagamento - soma)
