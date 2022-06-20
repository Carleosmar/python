#059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print('*' * 50)

print('[1] somar \n[2] multiplicar \n[3] maior \n[4] Novos números \n[5] Para sair do programa')

escolha = int(input('Digite sua opção: '))

while escolha != 5:
    if escolha == 1:
        s = n1 + n2
        print('A somatória dos numeros é {} valores' .format(s))
        sleep(2)
        print('[1] somar \n[2] multiplicar \n[3] maior \n[4] Novos numeros \n[5] Para sair do programa')

        print('*' * 50)
        escolha = int(input('Digite outra opção: '))

    elif escolha == 2:
        mult = n1 * n2
        print('A multiplicação dos numeros é {} valores' .format(mult))
        sleep(2)
        print('[1] somar \n[2] multiplicar \n[3] maior \n[4] Novos numeros \n[5] Para sair do programa')

        print('*' * 50)

        escolha = int(input('Digite outra opção: '))

    elif escolha == 3:
        if n1 > n2:
            print('O 1º valor {} é maior que o 2º valor {}' .format(n1, n2))
        else:
            print('O 2º valor {} é maior que o 1º valor {}' .format(n2, n1))
        sleep(2)

        print('[1] somar \n[2] multiplicar \n[3] maior \n[4] Novos numeros \n[5] Para sair do programa')

        print('*' * 50)
        escolha = int(input('Digite outra opção: '))
        print('*' * 50)
    elif escolha == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro valor: '))
        sleep(2)

        print('[1] somar \n[2] multiplicar \n[3] maior \n[4] Novos numeros \n[5] Para sair do programa')

        escolha = int(input('Digite sua opção: '))

print('OK PROGRAMA FINALIZADO')




