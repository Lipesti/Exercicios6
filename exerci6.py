#Exercicio 6 
#Faça um programa que lê as duas notas parciais obtidas por um aluno numa
#disciplina ao longo de um semestre, e calcule a sua média. 

nt1 = float(input('Digite sua primeira nota parcial: '))
nt2 = float(input('Digite sua segunda nota parcial: '))

media = (nt1+nt2)/2

if media == 9.0 and 10.0:
    print('Condição: A ')
    print('APROVADO')
elif media >= 7.5 and 8.9:
    print('Condição: B ')
    print('APROVADO')
elif media >= 6.0 and 7.4:
    print('Condição: C ')
    print('APROVADO')
elif media >= 4.0 and 5.9:
    print('Condição: D ')
    print('REPROVADO')
else:
    if media < 4:
        print('Condição: E ')
        print('REPROVADO')
