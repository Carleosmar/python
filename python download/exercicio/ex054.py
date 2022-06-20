#054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
#não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Qual o ano nasceu a {}ª pessoa: ' .format(c)))
    idade = ano_atual - ano
    if idade > 17:
        maior = maior + 1
    elif idade <= 17:
        menor = menor + 1

print('Tem {} maiores de idade e {} menores de idade' .format(maior, menor))









