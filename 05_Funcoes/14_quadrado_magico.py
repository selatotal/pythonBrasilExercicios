def geraQuadradoMagico():
    size = 3
    max = size * size
    quadrado = [0] * 3
    for i in range(0, 3):
        quadrado[i] = [0] * 3
    x = 0
    y = 1
    quadrado[x][y] = 1

    for z in range(2, max + 1):
        old_x = x
        old_y = y
        x -= 1
        y += 1

        if (x < 0):
            x = size - 1
        if (y >= size):
            y = 0

        print '%d %d' % (x, y)
        if (quadrado[x][y] == 0):
            quadrado[x][y] = z
        else:
            x = old_x + 1
            y = old_y
            if (x > size):
                x = 0
            quadrado[x][y] = z
    return quadrado


def imprimeQuadrado(quadrado):
    for i in quadrado:
        for j in i:
            print '%d\t' % (j),
        print

# Funcao principal
quadrado = geraQuadradoMagico()
imprimeQuadrado(quadrado)
