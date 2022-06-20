#041: A Confederação Nacional de Natação precisa de um programa que
#leia o ano de nascimento de um atleta e mostre sua categoria,
#de acordo com a idade:

#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date
ano_atual = date.today().year

ano = int(input('digite seu ano de nascimento: '))

categoria = ano_atual-ano

if categoria <= 9:
    print('Sua idade é {} anos e sua categoria é MIRIM' .format(categoria))
elif 10 < categoria <= 14:
    print('Sua idade é {} anos e sua categoria é INFANTIL' .format(categoria))
elif 15 < categoria <= 19:
    print('Sua idade é {} anos e sua categoria é JÚNIOR' .format(categoria))
elif 16 < categoria <= 25:
    print('Sua idade é {} anos e sua categoria é SÊNIOR' .format(categoria))
elif categoria > 25:
    print('Sua idade é {} anos e sua categoria é MASTER' .format(categoria))


