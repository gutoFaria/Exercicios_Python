# Faça um programa que pergunte o preço de três produtos e 
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

n1 = float(input('Digite o valor primeiro produto:'))
n2 = float(input('Digite o valor segundo produto:'))
n3 = float(input('Digite o valor terceiro produto:'))

if n1 < n2 and n1 < n3:
    print('O valor do menor produto é: ' + str(round(n1)))
elif n2 < n1 and n2 < n3:
    print('O valor do menor produto é: ' + str(round(n2)))
elif n3 < n1 and n3 < n2:
    print('O valor do menor produto é: ' + str(round(n3)))