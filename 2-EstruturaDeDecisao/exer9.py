# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

if n1 < n2 and n2 < n3:
    print(str(n3) + ' ' + str(n2) + ' ' + str(n1))
elif n1 < n1 and n3 < n2:
    print(str(n2) + ' ' + str(n3) + ' ' + str(n1))
elif n2 < n1 and n1 < n3:
    print(str(n3) + ' ' + str(n1) + ' ' + str(n2))
elif n2 < n1 and n3 < n1:
    print(str(n1) + ' ' + str(n3) + ' ' + str(n2))
elif n3 < n1 and n1 < n2:
    print(str(n2) + ' ' + str(n1) + ' ' + str(n3))
elif n3 < n2 and n2 < n1:
    print(str(n1) + ' ' + str(n2) + ' ' + str(n3))