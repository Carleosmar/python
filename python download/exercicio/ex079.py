#079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
#exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

while True:
    v = (int(input('Digite um valor: ')))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso')
    else:
        print('valor duplicado! Não vou adicionar...')
    conti = str(input('Desejar continuar? [S/N] ')).upper()
    if conti == 'N':
        break

print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')



