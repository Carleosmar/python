#043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
#de acordo com a tabela abaixo:

#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso/(altura*altura)

if imc < 18.5:
    print('Seu Indice de Massa Corporal é {:.2f}Kg/m2 e vc está abaixo do peso' .format(imc))
elif 18.5 < imc <= 25:
    print('Seu Indice de Massa Corporal é {:.2f}Kg/m2 e você está no Peso Ideal' .format(imc))
elif 25 < imc <= 30:
    print('Seu Indice de Massa Corporal é {:.2f}Kg/m2 e você está no Sobrepeso' .format(imc))
elif 30 < imc <= 40:
    print ('Seu Indice de Massa Corporal é {:.2f}Kg/m2 e você está com obesidade' .format(imc))
elif imc > 40:
    print('Seu Indice de Massa Corporal é {:.2f}Kg/m2 e você está com Obesidade Mórbida' .format(imc))

