#6- crie um algoritmo que leia um numero e mostre o seu dobro,  triplo e raiz quadrada?

n = int(input('\033[1;35;46mDigite um numero:\033[m '))
#c = pow(n, 1/2) A Função pow é uma funçaõ de potencia

print('O dobro de {} É {} \nE o triplo  {} \nSua raiz quadrada é {:.2f}' .format(n, (n*2), (n*3), (n**0.5)))

