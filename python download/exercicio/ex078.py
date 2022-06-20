#078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
#menor valor digitado e as suas respectivas posições na lista.

valores = []
cont = maior = menor = 0

for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
    if p == 0:
        maior = menor = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        if valores[p] < menor:
            menor = valores[p]

print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()

'''for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
print('=-'* 40)
print(f'O maior valor digitado foi {max(valores)} nas posições {valores.index(max(valores))}...')
print(f'O menor valor digitado foi {min(valores)} nas posições {valores.index(min(valores))}...')'''