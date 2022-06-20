#066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = s = n = 0
#n = int(input('Digite um valor [Para interrompe digite 999]: '))

while True:
    s += n
    n = int(input('Digite um valor [Para interrompe digite 999]: '))
    if n == 999:
        break
    cont += 1

print(f'Foram digitados {cont} valores e a somar entre eles é {s}')




