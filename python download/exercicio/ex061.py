#061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * r


while pt <= decimo:
    print(pt, end=' -> ')
    pt += r
print('FIM')


'''for c in range(pt, decimo + r, r):
   print(c, end= ' -> ')
print('fim')'''