#029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00
#por cada Km acima do limite

v = float(input('Digite sua velocidade: '))

valor = v - 80

if v > 80:
    print('Com a velocidade {} você está acima da velocidade permitida e sua multa é R${:.2f}' . format(v, valor*7))
else:
    print('Parabéns você está na velocidade permitida')
