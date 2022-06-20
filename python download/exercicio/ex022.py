#022: Crie um programa que leia o nome completo de uma pessoa e mostre:

#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras aotodo (sem considerar espaços)
#- Quantas letras tem o primeiro nome

nm = str(input('Digite seu nome completo: '))

print('Seu nome é em maiuscula {}' .format(nm.upper()))
print('Seu nome é em minuscula {}' .format(nm.lower()))
print('Seu nome tem {} letras' .format(len(nm) - nm.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nm.find(' ')))
