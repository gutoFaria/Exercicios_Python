# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metrosQuadradados = float(input('Entre com metros quadrados da área a ser pintada: '))
litrosDeTinta = 3 * metrosQuadradados
latas = litrosDeTinta / 18
precoTotal = latas * 80

print('Latas de tintas a serem compradas: ' + str(latas))
print('Preço total:R$ ' + str(round(precoTotal,2)))
