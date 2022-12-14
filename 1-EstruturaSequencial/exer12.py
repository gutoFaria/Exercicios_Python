# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Entre com a sua altura: '))

pesoIdeal = (72.7 * altura) - 58

print('Seu peso ideal é de: ' + str(round(pesoIdeal,2)) + ' kg')