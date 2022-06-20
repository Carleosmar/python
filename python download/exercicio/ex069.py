#069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:

#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

cont = h = f = 0

while True:
    idade = int(input('Idade: '))
    sx = ' '
    while sx not in 'MF':
        sx = str(input('Informe sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sx == 'M':
        h += 1
    if sx == 'F' and idade < 20:
        f += 1
    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Desejar continua [S/N]: ')).strip().upper()[0]
    if seguir == 'N':
        break

print(f'Tem {cont} pessoas com mais de 18 anos')
print(f'Tem {h} homens cadastrados e {f} mulheres com menos de 20 anos')
