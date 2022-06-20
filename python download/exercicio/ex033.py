#033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('primeiro numero: '))
b = int(input('segundo numero: '))
c = int(input('terceiro numero: '))

if a > b and b > c:
    print('O maior numero é {} e o menor numero é {}' .format(a, c))
elif a > c and c > b:
    print('O maior numero é {} e o menor numero é {}' .format(a, b))
elif b > a and a > c:
    print('O maior numero é {} e o menor numero é {}' .format(b, c))
elif b > c and c > a:
    print('O maior numero é {} e o menor numero é {}' .format(b, a))
elif c > b and b > a:
    print('O maior numero é {} e o menor numero é {}' .format(c, a))
elif c > a and a > b:
    print('O maior numero é {} e o menor numero é {}' .format(c, b))




