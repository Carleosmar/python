#074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
#de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint
maior = 0
menor = 0
cont = 0
tupla = tuple(randint(1, 10) for i in range (5))
print(tupla)

for num in tupla:
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')





