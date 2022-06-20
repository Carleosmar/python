#10- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# #considere U$: 1,00= R$ 3,27

din = float(input('Digite qual valor você tem na sua carteira: R$ '))
dolar = 3.27
quant = din/dolar
print('com R${:.2f} voce pode compra US${}{:.2f}' .format(din, '\033[32m', quant))

