#13- faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

sal = float(input('digite seu salario: '))
aum = sal*15/100+sal
print('O funcionario que recebe o salario de R${}{:.2f}{} com um aumento de 15% passar a receber: R${}{:.2f}' .format('\033[34m', sal, '\033[m', '\033[32m', aum))
