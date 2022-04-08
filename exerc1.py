#Exercicio 1 
#Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas.
#Faça um programa em Python que receba o salário fixo do funcionário e o valor de suas vendas.
#calcule e mostre a comissão e o salário final do funcionário.

salarioF = float(input('Digite o seu Salario R$: '))
valorVendas = float(input('Digite o valor da suas vendas R$: '))

comissao = valorVendas*0.04
salarioF += comissao

print(f'Comissão: R$ {comissao:.2f}')
print(f'Comissão: R$ {salarioF:.2f}')