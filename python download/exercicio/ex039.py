#039: Faça um programa que leia o ano de nascimento de um jovem e
#informe, de acordo com a sua idade, se ele ainda vai se alistar ao
#serviço militar, se é a hora exata de se alistar ou se já passou do
#tempo do alistamento. Seu programa também deverá mostrar o tempo que
#falta ou que passou do prazo

from datetime import date

ano_atual = date.today().year
ano = int(input('Digite o ano que você nasceu: '))

idade = ano_atual-ano
alista = 18-idade

if idade < 18:
    print('Falta {} ano(s) para você de alistar' .format(alista))
elif idade == 18:
    print('Você tem {} anos e já está na hora de vc se alistar' .format(idade))
else:
    print('Voce deveria ter se alistado há {} ano(s)' .format(idade-18))


