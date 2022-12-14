# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

F = float(input('Digite o valor da temperatura em Fahrenheit: '))
C = 5 * ((F-32)/9)

print('A temperatura em Celsius é: ' + str(round(C,1)) + ' °C')