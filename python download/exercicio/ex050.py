#050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s = s + n
        cont += 1
print('A contagem dos numeros pares foram {} e sua soma foi: {}' .format(cont, s))
