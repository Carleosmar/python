#016: Crie um programa que leia um número Real qualquer pelo teclado e
#mostre na tela a sua porção Inteira.

from math import  trunc
n = float(input('Digite um numero: '))
porint = trunc(n)
print('O numero digitado foi {} e o numero inteiro é {}' .format(n, porint))
