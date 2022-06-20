#11- Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para
#pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m².

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg*alt
litro = 2
quant = area/litro
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m² de parede\n que equivale a {} litros de tinta que serão gastos.' .format(larg, alt, area, quant))
