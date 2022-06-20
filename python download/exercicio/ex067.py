#067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
#pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('=' * 50)
print('TABUADA')
print('=' * 50)

r = cont = 0
ntab = int(input('Digite um numero para ver sua tabuada: '))
while True:
    while cont <= 10:
        r = ntab * cont
        print(f'{ntab} x {cont} = {r}')
        cont += 1
    ntab = int(input('Digite um numero para ver sua tabuada: '))
    if ntab < 0:
        break
    cont = 0
print('TABUADA ENCERRADA')


