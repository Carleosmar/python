#081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    sn = str(input('Desejar continuar [S/N]: ')).upper()
    if sn == 'N':
        break
lista.sort(reverse=True)

print('-=' * 30)
print(f'Foram digitados {len(lista)} numeros')
print(f'Os numeros digitados em ordem decrescente foram {lista}')

if 5 in lista:
    print('O Valor 5 está na lista')
else:
    print('O valor 5 não se encontra na lista')
