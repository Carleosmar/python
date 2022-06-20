#058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
#o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep

mais1 = 1

print('*' * 40)
a1 = int(input('Em qual numero estou pensando entre 0 e 10: ')) # Numero que o jogador está pensando
print('*' * 40)
escolha = random.randint(0, 10) # faz o computador "PENSAR"
print('PROCESSANDO....')
sleep(3)
print('O numeror que estou pensando é {}' .format(escolha))

while a1 != escolha:
    print('*' * 40)
    print('Eu pensei em  {} e você em {}. Logo você errou' .format(escolha, a1))
    print('*' * 40)
    sleep(3)
    a1 = int(input('Em qual numero estou pensando agora entre 0 e 10: '))  # Numero que o jogador está pensando
    print('*' * 40)
    escolha = random.randint(0, 10)  # faz o computador "PENSAR"
    print('PROCESSANDO....')
    sleep(3)
    print('O numeror que estou pensando é {}'.format(escolha))

    mais1 += 1

if a1 == escolha:
    print('Voce acertou!!! E sua quantidade de tentativa foi {}' .format(mais1))
    print('FIM DE JOGO')

