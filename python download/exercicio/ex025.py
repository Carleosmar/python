#025: Crie um programa que leia o nome de uma pessoa e
#diga se ela tem "SILVA" no nome.


nm = str(input('Digite seu nome: ')).strip().title()
print('Olá seu nome é {}' .format(nm))
print('silva' in nm.lower())

