#024: Crie um programa que leia o nome de uma cidade diga
#se ela começa ou não com o nome "SANTO".

cid =str(input('Digite o nome de uma cidade : ')).strip()
print(cid[:5].upper() == 'SANTO')



#print('Santo' in cid[:5])

