#068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0

while True:
    print('=' * 60)
    print('Bora Jogar PAR OU IMPAR')
    print('=' * 60)
    n = int(input('Digite um valor: '))
    escolha = randint(0, 10)
    r = n + escolha
    resto = r % 2
    p_i = ' '
    while p_i not in 'PI':
        p_i = str(input('Você quer PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    if p_i == 'P':
        if resto == 0:
            print('Você venceu')
        else:
            print('Você Perdeu')
            break
    if p_i == 'I':
        if resto == 1:
            print('Voce ganhou')
        else:
            print('Você perdeu')
            break
    cont += 1
print(f'ESSA VOCÊ PERDEU O COMPUTADOR ESCOLHEU {escolha}')
print(f'Você ganhou {cont} vezes')

