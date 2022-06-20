#12- faça um algoritmo que leia o preço de um produto e mostre seu novo preço,  com 5% de desconto.

preco = float(input('Digite o preço? R$: '))
a = preco*5/100
b = preco-a
print('O valor do produto que custava R${}{:.2f}{} com 5% de desconto fica: R${}{:.2f}' .format('\033[31m', preco, '\033[m', '\033[34m', b))
