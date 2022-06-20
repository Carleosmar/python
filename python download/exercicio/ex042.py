#042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
#mostrar que tipo de triângulo será formado:

#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados dife

print('criando triangulo')
print('-' * 30)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a+b > c and b+c > a and a+c > b:
    print('O triangulo pode ser feito.', end='')
    if a == b == c:
        print('E ele é EQUILÁTERO')
    elif a != b != c != a:
        print('E ele é ESCALENO')
    else:
        print('E ele é ISÓCELES')
else:
    print('O triangulo não pode ser feito.')
