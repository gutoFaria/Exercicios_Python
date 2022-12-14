# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

l = float(input('Digite o valor do lado do quadrado: '))
area = l**2
dobroArea = 2 * area

print('A = ' + str(area))
print('Dobro da área: ' + str(dobroArea))