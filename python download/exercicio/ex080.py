#080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()).No final, mostre a lista ordenada na tela.

n = []
for p in range(0, 5):
    num = int(input('Digite um valor: '))
    if p == 0 or num > n[-1]:
        n.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(n):
            if num <= n[pos]:
                n.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {n}')





