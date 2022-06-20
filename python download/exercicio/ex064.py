'''064: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

print('')
valor = int(input('Digite o valor que deseja somar. [999 para parar]: '))
n = 0
cont = 0

while n != 999:
    exato = valor + n
    valor = int(input('Digite um valor [999 para parar]: '))
    n = valor
    valor = exato
    cont += 1
print('O resultado é : {} e você digitou {} numeros' .format(valor, cont))


