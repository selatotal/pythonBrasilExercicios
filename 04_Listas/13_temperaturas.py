meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
temperaturas = {}

for mes in meses:
    temperaturas[mes] = float(
        raw_input('Informe a temperatura media do mes de %s: ' % mes))

somaTemperaturas = 0.0
for temperatura in temperaturas.values():
    somaTemperaturas += temperatura

mediaTemperaturaAnual = somaTemperaturas / 12.0

print 'Temperaturas acima da media anual: %.2f' % mediaTemperaturaAnual
for mes in meses:
    if (temperaturas[mes] >= mediaTemperaturaAnual):
        print '%s - %.2f' % (mes, temperaturas[mes])
