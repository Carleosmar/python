#060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Diga o numero que você quer fatora: '))
c = n
fat = 1
print('Calculando {}! = ' .format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')

    fat *= c
    c -= 1

print('{}' .format(fat))


