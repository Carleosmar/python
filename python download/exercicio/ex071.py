#071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 60)
print('{:^60}' .format('BANCO CARLE'))
print('=' * 60)
tot50 = tot20 = tot10 = tot1 = 0
ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1
valor = int(input('Que valor você quer sacar? R$: '))
while True:
    if valor >= ced50:
        valor -= ced50
        tot50 += 1
    if valor >= 20 and valor < ced50:
        valor -= ced20
        tot20 += 1
    if valor >= ced10 and valor < ced20:
        valor -= ced10
        tot10 += 1
    if valor >= ced1 and valor < ced10:
        valor -= ced1
        tot1 += 1
    if valor == 0:
        break
if tot50 > 0:
    print(f'Total de {tot50} cédulas de R$50')
if tot20 > 0:
    print(f'Total de {tot20} cédulas de R$20')
if tot10 > 0:
    print(f'Total de {tot10} cédulas de R$10')
if tot1 > 0:
    print(f'Total de {tot1} cédulas de R$1')

print('Volte sempre ao BANCO CARLE!!!!! Tenha um Bom dia!')


