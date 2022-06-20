#088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
#gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogos = []
sorteio = []
tot = 1
print('-' * 30)
print('JOGO DA MEGA SENA')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie: '))
while tot <= quant:
    cont = 0
    while True:
        jogo = randint(1,60)
        if jogo not in jogos:
            jogos.append(jogo)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    sorteio.append(jogos[:])
    jogos.clear()
    tot += 1

for i , s in enumerate(sorteio):
    print(f'Jogo{i+1}: {s}')
    sleep(1)
print('BOA SORTEEEEE.......')


