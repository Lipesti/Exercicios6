#Exercicio 2 
#- Faça um programa em Python que solicite ao usuário uma quantidade de
#segundos, calcule e exiba a quantidade de horas, minutos e segundos.

segundos = int(input('Digite a quantidade de segundos: '))
horas = segundos // 3600
minutos = segundos % 3600 //60
segundos = segundos%60
print(horas, 'Hora', minutos, 'minutos e', segundos, 'Segundos')