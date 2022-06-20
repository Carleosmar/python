#9- faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada.

n = int(input('digite um numero para saber sua tabuada: '))
mais1 = 0

print('-' * 15)
print('A tabuada de {}: ' .format(n))
print('-' * 15)

while(mais1 <= 10):
    print('{} x {:2} = {}{}{}' .format(n, mais1, '\033[31m', (n*mais1), '\033[m'))
    mais1 = mais1+1

