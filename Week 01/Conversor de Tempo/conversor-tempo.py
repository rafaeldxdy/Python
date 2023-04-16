horas = int(input('Escreva quantas horas são: '))
minutos = int(input('Escreva quantos minutos são: '))
segundos = int(input('Escreva quantos segundos são: '))
segundos = horas*3600 + minutos*60 + segundos
print('São exatamente: ', segundos, 'segundos')

horas = segundos//3600
minutos = horas*60
print('São: ', horas, 'horas ou ', minutos, 'minutos ou ', segundos, 'Segundos')