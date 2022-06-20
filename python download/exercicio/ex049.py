#049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for.

n = int(input('digite um numero para saber sua tabuada: '))
mais1 = 0
print('-' * 15)
print('A tabuada de {} é: ' .format(n))
print('-' * 15)
for c in range(0, 11):
    print('{} X {} = {}' .format(n, c, n*c))
print('Fim de tabuada')
