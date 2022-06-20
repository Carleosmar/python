#045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)

print('Vamos jogar Jokenpô????')
print('-'*40)

print('''ESCOLHA:
[0] pedra
[1] papel
[2] tesoura''')
print('-'*40)

joga = int(input('Qual a sua jogada? '))

print('-'*40)

print('jo')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('Jogador jogou {}' .format(itens[joga]))
print('Computador jogou {}' .format(itens[computador]))


print('-'*30)

if joga == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('Computador GANHOU')
    elif computador == 2:
        print('Jogador GANHOU')
    else:
        print('jogada invalida')
elif joga == 1:
    if computador == 0:
        print('Jogador GANHOU')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('jogada invalida')
elif joga == 2:
    if computador == 0:
        print('COMPUTADOR GANHOU')
    elif computador == 1:
        print('Jogador GANHOU')
    elif computador == 2:
        print('EMPATE')
    else:
        print('jogada invalida')
else:
    print('OPÇÃO INVALIDA')

