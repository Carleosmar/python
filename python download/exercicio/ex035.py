#035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
#elas podem ou não formar um triângulo.

print('criando triangulo')
print('-' * 30)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a+b > c and b+c > a and a+c > b:
    print('O triangulo pode ser feito.')
else:
    print('O triangulo não pode ser feito.')

