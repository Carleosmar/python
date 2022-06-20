#8- Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

valor = float(input('Digite um valor em metros: '))
cm = valor*100
mm = valor*1000
dm = valor*10
dam = valor*0.1
hm = valor*0.01
km = 0.001
print('Tal medida {}m é: \nem centimetros: {}cm \nmilimetros {}mm \ndecimetro {}dm \ndecametro {}dam \nhectometro {} \nQuilometro {} ' .format(valor, cm, mm, dm, dam, hm, km))
