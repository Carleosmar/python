#034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
#seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os
#inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite seu salario: R$ '))

if sal >= 1250.00:
    print('Seu salario é R${:.2f} e com um aumento de 10% fica R${:.2f}' .format(sal, sal+(sal*10/100)))
else:
    print('Seu salario é R${:.2f} e com um aumento de 15% fica R${:.2f}' .format(sal, sal+(sal*15/100)))
