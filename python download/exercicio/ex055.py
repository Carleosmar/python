#055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 1000

for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso foi {}Kg e o menor peso foi {}Kg'.format(maior, menor))




