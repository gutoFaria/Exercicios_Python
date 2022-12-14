# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# d. Para homens: (72.7*h) - 58
# e. Para mulheres: (62.1*h) - 44.7

sexo = str(input('Digte M para masculino e F para feminino:'))
altura = float(input('Entre com a sua altura: '))

if sexo == 'M':
    pesoIdeal = (72.7*altura) - 58
    print('Seu peso ideal é de: ' + str(round(pesoIdeal,2)))
elif sexo == 'F':
    pesoIdeal = (62.1*altura) - 44.7
    print('Seu peso ideal é de: ' + str(round(pesoIdeal,2)))