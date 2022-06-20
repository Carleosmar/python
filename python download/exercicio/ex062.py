'''062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * r

nome = str(pt)
while pt != 0:
    if pt <= decimo:
        print(pt, end=' -> ')
        nome = nome + ' -> ' + str(pt)
        pt += r
    elif pt >= decimo:
        n = int(input('\nQuantos mais alguns termos você desejar: '))
        decimo = pt + (n - 1) * r
        if n == 0:
            pt = 0

print(nome)

'''while pt <= decimo:
    print(pt, end=' -> ')
    pt += r
print('FIM')'''