#Exercicio 5 

import math

area = int(input('Digire a área a ser pintada (em m²): '))

tinta = area/3

latas = math.ceil(tinta/18)

print(f'Quantidade de latas necessarias: {latas} ')
print(f'Valor das tintas R${latas*80:.2f} ')
