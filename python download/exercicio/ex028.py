#028: Escreva um programa que faça o computador "pensar" em um número
#inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
#número escolhido pelo computador. O programa deverá escrever na tela
#se o usuário venceu ou perdeu.

import random
from time import sleep
print('*' * 40)
a1 = int(input('Em qual numero estou pensando entre 0 e 5: ')) # Numero que o jogador está pensando
print('*' * 40)
escolha = random.randint(0, 5) # faz o computador "PENSAR"
print('PROCESSANDO....')
sleep(3)
print('O numeror que estou pensando é {}' .format(escolha))

if a1 == escolha:
    print('Voce acertou o número.')
else:
    print('Você errou eu pensei no numero {} e você pensou no {}' .format(escolha, a1))


