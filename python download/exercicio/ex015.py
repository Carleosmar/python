#15- Escreva um programa que pergunte a quantidade de Km percorridos por
#um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
#e R$0,15 por Km rodado.

dias = int(input('Há quantos dias esse carro foi alugado? '))
km = float(input('Quantos quilometros você pecorreu? '))


preco = (km*0.15)+(dias*60.00)
print('Com a quantidade de {} dias e {}km o valor do aluguel ficou {:.2f}' .format(dias, km, preco))
