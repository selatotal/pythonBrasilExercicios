import random

dado = [0] * 6

for i in range(0, 100):
    lancamento = random.randint(0, 5)
    dado[lancamento] += 1

for i in range(0, 6):
    print '%d - %d' % (i + 1, dado[i])
