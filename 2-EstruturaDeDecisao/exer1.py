# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite um número:'))
n2 = int(input('Digite o segundo número:'))

if n1 > n2:
    print('O maior número digitado é: ' + str(n1))
else:
    print('O maior número digitado é: ' + str(n2))