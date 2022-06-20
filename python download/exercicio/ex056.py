#056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mediaidade = 0
maisvei = 0
nomevei = str
count_mulher = 0

for c in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Informe seu sexo[M/F]: ')).upper()
    mediaidade += idade
    print('-' * 30)
    if idade > maisvei and sexo == 'M':
        maisvei = idade
        nomevei = nome
    elif idade < 20 and sexo == 'F':
        count_mulher += 1


print('media da idade é {} a idade do homem mais velho é {} e o seu nome é {} e temos {} mulheres com menos de 20 anos' .format(mediaidade/4, maisvei, nomevei, count_mulher))

