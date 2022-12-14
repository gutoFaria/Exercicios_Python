# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
print('Cálculo da área de um círculo \n')
r = float(input('Digte o raio do círculo: '))

area = math.pi * (r**2)

print('Área do círculo de r = ' + str(r) + ' = ' + str(round(area,2)))