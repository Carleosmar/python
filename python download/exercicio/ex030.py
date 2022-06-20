#030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou
#ÍMPAR.

n = int(input('Digite um numero: '))

if n % 2 == 0:
    print('Você digitou o numero {} e ele é par.' .format(n))
else:
    print('Voce digitou o numero {} e ele é impar' .format(n))
