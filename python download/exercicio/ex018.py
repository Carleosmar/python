#018: Faça um programa que leia um ângulo qualquer e mostre na tela o
#valor do seno, cosseno e tangente desse ângulo

import math

a = float(input('Digite um angulo quaquer: '))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O angulo que vc digitou é {} e o\n Seno é {:.2f}\n cosseno é {:.2f}\n tangente é {:.2f}' .format(a, sen, cos, tan))
