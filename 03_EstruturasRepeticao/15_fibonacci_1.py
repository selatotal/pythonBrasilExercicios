termo = 0
while (termo <= 0):
    termo = int(raw_input('Voce quer a serie de Fibonacci ate qual termo: '))
    if (termo <= 0):
        print 'O termo deve ser positivo!'

primeiro = 0
print primeiro
segundo = 1
for i in range(1, termo):
    print segundo
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
