#Faça um programa que leia na tela algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possiveis sobre ele.

leia = input('Digite algo: ')
print('É um tipo primitivo', type(leia))
print('Só tem espaços', leia.isspace())
print('É numerico', leia.isnumeric())
print('É alfabetico', leia.isalpha())
print('É alfanumerico:', leia.isalnum())
print('Está em maiuscula:', leia.isupper())
print('Está em minuscular:', leia.islower())



