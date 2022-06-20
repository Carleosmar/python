#073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'America-MG', 'Atlético-GO', 'Santos',
          'Ceará', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('=-' * 20)
print(f'Lista de times do brasileirão: {tabela}')
print('=-' * 20)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('=-' * 20)
print(f'Os 4 ultimos colocados: {tabela[-4:]}')
print('=-' * 20)
print(f'Times em ordem alfabeticas: {sorted(tabela)}')
print('=-' * 20)
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')



