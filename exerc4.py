#Exercicio 4
#Faça um programa em Python que solicite ao usuário sua altura e sexo,
#calcule e imprima o seu peso ideal. Utilize a seguinte convenção:
#▪ Para homens: (72.7*h) – 58
#▪ Para mulheres: (62.1*h) – 44.7

alt = float(input('Digite sua altura em metros: '))
sexo = input('Digite o seu genero h/m: ')

if sexo == 'H' or 'h':
   peso = (72.7*alt)-58
elif sexo == 'M' or 'm':
   peso = (62.1*alt)-44.7
else:
    peso = 0 
    
if peso == 0: 
    print('Sexo invalido')
else:
    print(f'O peso ideal {peso:.2f} para essa pessoa')