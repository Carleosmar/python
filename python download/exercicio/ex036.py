#036: Escreva um programa para aprovar o empréstimo bancário para a
#compra de uma casa. Pergunte o valor da casa, o salário do comprador
#e em quantos anos ele vai pagar. A prestação mensal não pode
#exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o seu salario: R$ '))
anos = int(input('Em quanto anos você vai paga: '))

minimo = sal*30/100
prestacao = anos*12
parcela = valor_casa/prestacao

if parcela < minimo:
    print('Seu emprestimo foi aprovado e você pagará R${:.2f} mensal' .format(parcela))
else:
    print('Seu emprestimo não foi aprovado já que exceder 30% do seu salario e valor de suas parcelas ficariam  R$ {:.2f}' .format(parcela))

