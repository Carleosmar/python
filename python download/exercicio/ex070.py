#070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print('-' * 60)
print('{:^60}' .format('Loja Carleosmar'))
print('-' * 60)
tot = prod = menor = mais1 = 0
nm = ' '
while True:
    np = str(input('Informe nome do produto: '))
    preco = float(input('Informe o preço R$: '))
    tot += preco
    mais1 += 1
    if preco > 1000:
        prod += 1
    if mais1 == 1 or preco < menor:
        menor = preco
        nm = np
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Desejar continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break

print(f'Total gasto foi R$: {tot:.2f}')
print(f'Tem {prod} produtos que custam mais de R$ 1000,00')
print(f'O nome do produto mais barato é {nm} e o seu valor é R$: {menor:.2f}')