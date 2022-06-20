# 037: Escreva um programa em Python que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal

n = int(input('Digite um numero: '))
esc = int(input('Para converte em binario escolha 1, para octal escolha 2 e para hexadecimal escolha 3: '))

if esc == 1:
    print('O numero em binario  é: {}' .format(bin(n)[2:]))
elif esc == 2:
    print('O numero em octal é: {}' .format(oct(n)[2:]))
elif esc == 3:
    print('O numero hexadecimal é: {}'.format(hex(n)[2:]))
else:
    print('Você não escolheu nenhuma das opções')
    
