#076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-'* 40)
print(f'{"LISTAGEM DE PREÇOS": ^40}')
print('-'* 40)

listagem = ('Lapis....................R$  1.75',
            'Borracha.................R$  2.00',
            'Estojo...................R$  25.00',
            'Caderno..................R$  15.90',
            'Transferidor.............R$  4.20',
            'Compasso.................R$  4.20',
            'Mochila..................R$  120.32',
            'canetas..................R$  20.00',
            'Livro....................R$  34.00')

for lista in listagem:
    print(lista)
print('-'* 40)
