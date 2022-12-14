# Faça um Programa que pergunte quanto você ganha por hora e o 
# número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Quanto você ganha por hora: '))
numeroHoras = float(input('Quantas horas foram trabalhadas no mês: '))

salario = valorHora * numeroHoras

print('Seu salário no mês é: ' + str(salario))