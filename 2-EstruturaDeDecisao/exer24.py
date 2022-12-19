# Faça um Programa que leia 2 números e em seguida pergunte ao 
# usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# j. par ou ímpar;
# k. positivo ou negativo;
# l. inteiro ou decimal.

n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))

print('Menu de Opções')
print('[1] SOMA')
print('[2] SUBTRAÇÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] DIVISÃO')
e = int(input('Entre com a sua escolha:'))
if e == 1:
    r = n1 + n2
    if r % 2 == 0:
        print(str(round(r,1)) + ' é um número par' )
    else:
        print(str(round(r,1)) + ' é um número impar' )
    
    if r > 0:
        print(str(round(r,1)) + ' é um número positivo' )
    else:
         print(str(round(r,1)) + ' é um número negativo' )
    
    if r.is_integer():
        print(str(round(r,1)) + ' é um número inteiro' )
    else:
        print(str(round(r,1)) + ' é um número decimal' )