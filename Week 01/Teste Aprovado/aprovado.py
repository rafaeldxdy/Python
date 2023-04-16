nota1 = int(input('Qual sua primeira nota? '))
nota2 = int(input('Qual sua segunda nota? '))
media = (nota1 + nota2) / 2
print('Sua média é: ', media)
if media < 60:
    print('Reprovado')
else:
    print('Aprovado')