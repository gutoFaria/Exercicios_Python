#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

d = int(input('Entre com o dia:'))
m = int(input('Entre com o mes:'))
a = int(input('Entre com o ano:'))

if m == 2 and d > 0 and d <= 28 and a > 0 and a <= 2022:
    print('Data válida!')
elif m == 4 or m == 7 or m == 9 or m == 11 and d > 0 and d <= 30 and a > 0 and a <= 2022:
    print('Data válida!')
elif m == 1 or m == 3 or m == 5 or m == 6 or m == 8 or m == 10 or m == 12 and d > 0 and d <=31 and a > 0 and a <= 2022:
    print('Data válida!')
else:
    print('Data inválida')
    

