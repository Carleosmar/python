#052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n+1):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print('Tem {} múltiplos acima de 2 e abaixo de {}' .format(mult, n))



