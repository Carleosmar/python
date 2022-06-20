#026: Faça um programa que leia uma frase pelo teclado e mostre
#quantas vezes aparece a letra "A",
# em que posição ela aparece
#a primeira vez e em que posição ela aparece a última vez.

frase = str(input(' Digite uma frase: ')).upper().strip()

print('Essa frase tem essa quantidade {} de letra A' .format(frase.count('A')))
#print('Essa frase tem essa quantidade {} de letra a minuscula' .format(frase.count('a')))

print('A posição que a letra A aparece pela primeira vez é {}' .format(frase.find('A')+1))
#print('A posição que a letra a aparece pela primeira vez é {}' .format(frase.find('a')+1))

print('A posição que a letra A aparece pela ultima vez é {}' .format(frase.rfind('A')+1))
#print('A posição que a letra a aparece pela ultima vez é {}' .format(frase.rfind('a')+1))
