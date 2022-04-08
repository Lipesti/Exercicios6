#Exercicio 7 

print('Cordenadas de um ponto P(x e y) ')
x = float(input('Digite as cordenadas de x: '))
y = float(input('Digite as cordenadas de y: '))

if x > 0 and y > 0:
    print(f'O ponto P ({x}, {y}) pertence ao 1º quadrante')
elif x < 0 and y > 0:
    print(f'O ponto P ({x}, {y}) pertence ao 2º quadrante')
elif x < 0 and y < 0:
    print(f'O ponto P ({x}, {y}) pertence ao 3º quadrante')
elif x > 0 and y < 0:
    print(f'O ponto P ({x}, {y}) pertence ao 4º quadrante')