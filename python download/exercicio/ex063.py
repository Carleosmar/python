#063: Escreva um programa que leia um número N inteiro qualquer e
#mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
import math

t = 0
s = 0
s2 = 1
fn = 1

n = int(input('Digite  quantos elementos da sequencia fibonacci você desejar ver: '))

d = math.ceil(n / 2)

while t < d:
    print(str(s) + ' -> ' + str(fn), end=' -> ')
    s2 = fn
    fn = fn + s + s2
    s = fn - s2


    t += 1

print('FIM')
