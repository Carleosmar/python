#7- desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a media.

nota1 = float(input('digite nota 1 '))
nota2 = float(input('digite nota 2 '))
r = (nota1+nota2)/2
print('De acordo com a nota {} e a nota {} a media é: {}{:.1f}{} ' .format(nota1, nota2, '\033[1;31;44m', r, '\033[m'))
