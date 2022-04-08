# Exercicio 9 

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

print('[1] Média')
print('[2] Diferença maior-menor')
print('[3] Produto')
print('[4] Divisão n1/n2')

opcao = int(input('Digite a sua opção: '))

if opcao == 1:
        media = (num1+num2)/2
        print(f'Média = {media}')
elif opcao == 2:
    dife = num1-num2
    print(f'Diferença = {dife}')
elif opcao == 3:
    prod = num1*num2
    print(f'Produto = {prod}')
elif opcao == 4:
    if num2 == 0:
        print('Impossivel dividir por 0')
    div = num1/num2
    print(f'Divisão = {div:.3f}')
else:
    if opcao != 4:
        print('Opção inválida')
    
        

