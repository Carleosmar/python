#023: Faça um programa que leia um número de 0 a 9999
#e mostre na tela cada um dos dígitos separados.

nm = int(input('Digite um numero entre 0 a 9999: '))

u = nm // 1 % 10
d = nm // 10 % 10
c = nm // 100 % 10
m = nm // 1000 % 10

#num = str(nm)
print('O numero digitado é: {}' .format(nm))
print('A sua unidade é {}' .format(u))
print('A sua dezena é {}' .format(d))
print('A sua centena é {}' .format(c))
print('O seu milhar é {}' .format(m))
