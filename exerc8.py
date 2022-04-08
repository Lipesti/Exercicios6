#Exercicio 8 

nome = input('Digite o seu nome: ')
horas = int(input('Informe as horas [0-23]: '))

if horas >= 5 and horas <= 12:
    print(f'Bom dia {nome}')

elif horas > 12 and horas <= 18:
    print(f'Boa tarde {nome}')

elif horas >= 19 and horas < 4:
     print(f'Boa noite {nome}')
