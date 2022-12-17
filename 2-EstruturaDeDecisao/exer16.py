# Faça um programa que calcule as raízes de uma equação do segundo grau, 
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as 
# consistências, informando ao usuário nas seguintes situações:
# a. Se o usuário informar o valor de A igual a zero, a equação não é do 
# segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raizes reais. 
# Informe ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math
print('Cálculo das raízes do segundo grau ax2 + bc + c')
print('Digite os valores das incognitas A, B  e C')
a = float(input('Digite o valor de A:'))
b = float(input('Digite o valor de B:'))
c = float(input('Digite o valor de C:'))
if a == 0:
    print('Não é uma equação de segundo grau.')

d = b**2 -(4 * a * c)
if d < 0:
    print('Delta menor que zero, a equação não possui raízes.')
r1 = (-b + math.sqrt(d)) / 2
r2 = (-b - math.sqrt(d)) / 2

if d == 0:
    print('A equação possui apenas uma raiz real: ' + str(round(r1,2)))
elif d > 0:
    print('A equação possui duas raiz reais: r1 = ' + str(round(r1,2)) + '   r2 = ' + str(round(r2,2)))

