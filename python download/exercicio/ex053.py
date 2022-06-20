#053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.


frase = str(input('Digite uma frase: ')).upper().replace(' ','')
print('Sua frase invertida fica: {}' .format(frase[::-1]))

if frase == frase[::-1]:
    print('A frase é um polidormo')
else:
    print('Não é um polidromo')


