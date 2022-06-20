#032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Digite um ano qualquer: '))
if ano ==0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('Esse ano {} é bissexto' .format(ano))
else:
    print('Esse ano {} não é bissexto' .format(ano))
