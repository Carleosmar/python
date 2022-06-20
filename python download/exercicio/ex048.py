#048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que
#se encontram no intervalo de 1 até 500.

print('Somando todos os numeros que são multiplos de 3 e que estão entre 1 e 500')
s = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s+=c
        cont += 1
print('A soma dos multiplos de 3 é: {} e foram contados {} valores' .format(s, cont))


