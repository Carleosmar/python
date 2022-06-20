#087: Aprimore o desafio anterior, mostrando no final:

#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
parmat = []
soma = terco = 0

for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-' * 30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            soma = matriz[l][c] + soma
    print()
terco = matriz[0][2] + matriz[1][2] + matriz[2][2]

print(f'Os valores pares são: {soma}')
print(f'A soma dos valores da terceira coluna é {terco}')

if matriz[1][0] > matriz[1][1] > matriz[1][2]:
    print(f'O maior valor da segunda coluna é {matriz[1][0]}')
elif matriz[1][0] > matriz[1][2] > matriz[1][1]:
    print(f'O maior valor da segunda coluna é {matriz[1][0]}')
elif matriz[1][1] > matriz[1][2] > matriz[1][0]:
    print(f'O maior valor da segunda coluna é {matriz[1][1]}')
elif matriz[1][1] > matriz[1][0] > matriz[1][2]:
    print(f'O maior valor da segunda coluna é {matriz[1][1]}')
elif matriz[1][2] > matriz[1][0] > matriz[1][1]:
    print(f'O maior valor da segunda coluna é {matriz[1][2]}')
elif matriz[1][2] > matriz[1][1] > matriz[1][0]:
    print(f'O maior valor da segunda coluna é {matriz[1][2]}')








