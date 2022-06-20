#057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo M P/ Masculino F P/ Feminino: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
        print('Opção invalida Digite Novamente')
        sexo = str(input('Informe seu sexo M P/ masculino F P/ Feminino: ')).strip().upper()
if sexo == 'M':
    print('Então seu sexo é Masculino')
elif sexo == 'F':
    print('Então seu sexo é Feminino')

