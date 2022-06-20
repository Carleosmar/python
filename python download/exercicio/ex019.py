#019: Um professor quer sortear um dos seus quatro alunos para apagar o
#quadro. Faça um programa que ajude ele, lendo o nome dos alunos e
#escrevendo na tela o nome do escolhido.

import random

nm1 = input('Digite o nome do aluno: ')
nm2 = input('Digite o nome do aluno: ')
nm3 = input('Digite o nome do aluno: ')
nm4 = input('Digite o nome do aluno: ')

lista = [nm1, nm2, nm3, nm4]
sorteio = random.choice(lista)

print('O aluno que irá apagar po quadro é: {}' .format(sorteio))
