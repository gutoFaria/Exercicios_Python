# Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# • Dicas:
# • Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# • Triângulo Equilátero: três lados iguais;
# • Triângulo Isósceles: quaisquer dois lados iguais;
# • Triângulo Escaleno: três lados diferentes;

print('Digite o valor dos 3 lados de um triângulo')
l1 = float(input('Digite o valor do primeiro lado:'))
l2 = float(input('Digite o valor do segundo lado:'))
l3 = float(input('Digite o valor do terceiro lado:'))

if (l1 + l2) > l3 or (l1 + l3) > l2 or (l3 + l2) > l1:
    print('Os lados formam um triangulo')
if l1 == l2 and l2 == l3:
    print('Triângulo Equilátero: três lados iguais;')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('Triângulo Isósceles: quaisquer dois lados iguais;')
elif l1 != l2 and l2 != l3:
    print('Triângulo Escaleno: três lados diferentes;')     