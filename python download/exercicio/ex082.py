#082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
#apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    n = int(input('Digite um numero: '))
    lista.append(n)

    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    resp = str(input('Desejar continuar [S/N]: ')).upper()
    if resp == 'N':
        break

print(f'Lista completa: {lista}')
print(f'Lista de pares: {lista_par}')
print(f"Lista de Ímpares: {lista_impar}")

