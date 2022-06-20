'''065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
count = menor = maior = s = 0

p = str('s').upper()

while p != 'N':
    n = int(input('Digite um valor: '))
    count += 1
    s += n

    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    p = str(input('Para continuar a digitar valores tecle S se não tecle N: ')).upper()

m = s/count
print('A quantidade de valores digitada foi {}' .format(count))
print('A média de todos os valores são {:.2f} o valor maior é {} e o menor é {}' .format(m, maior, menor))



