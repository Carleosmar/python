#044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço do produto: '))

valor1 = preco-(preco*10/100)
valor2 = preco-(preco*5/100)
valor3 = preco
valor4 = preco+(preco*20/100)

print('-'*40)

print('''CONDIÇÕES DE PAGAMENTO:  
[1] Avista DINHEIRO OU CHEQUE  
[2] Avista no cartão  
[3] Duas vezes no cartão  
[4] em até 3X ou mais: ''')

pag = int(input('Informe forma de pagamento: '))

if pag == 1:
    print('Com a opção escolhida para pagamento  o valor do produto será R${:.2f} e seu desconto e de 10%.' .format(valor1))
elif pag == 2:
    print('Com a opção escolhida para pagamento o valor do produto será R${:.2f} e o seu desconto é de 5%.' .format(valor2))
elif pag == 3:
    print('Sendo assim o pagamento é parcelado em 2X fica R${:.2f} e o  preço final será de R${:.2f} e esse é seu preço formal.' .format(preco/2, valor3))
elif pag == 4:
    totparc = int(input('Em quantas vezes vc quer parcela: '))
    parcela = valor4 / totparc
    print('Com essa opção para pagamento o valor do produto parcelado será de R${:.2f}.' .format(parcela))
    print('E o preço total será R${} com 20% de juros.' .format(valor4))
else:
    print('Opção invalida tente novamente')
