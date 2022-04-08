#Exercicio 3 
#Faça um programa que solicite ao usuário um número inteiro.
#Verifique e se ele é positivo, negativo ou nulo.

valor = int(input('Digite um numero para saber se é (Positivo/Negativo ou Nulo): '))

if valor > 0:
    print(f'O numero {valor} é positivo')
elif valor < 0:
    print(f'O numero {valor} é negativo')    
else:
    print(f'O numero {valor} é nulo') 