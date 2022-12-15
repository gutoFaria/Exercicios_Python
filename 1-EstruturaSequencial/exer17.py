# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00.
# • Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# • comprar apenas latas de 18 litros;
# • comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metrosQuadradados = float(input('Entre com metros quadrados da área a ser pintada: '))
litrosDeTinta = metrosQuadradados / 6
latas = litrosDeTinta / 18
galao = litrosDeTinta / 3.6

lataGrande = latas * 80
latasPequenas = latas * 25


print('Área: ' + str(metrosQuadradados))
print('Quantidade de tinta a ser comprada: ' + str(round(litrosDeTinta,0)))

print('\n')
print('Para latas de 18L ')
if litrosDeTinta % 18 != 0 :
    latas += 1;
    print('Quantidade de latas 18L: ' + str(round(latas,0)))
    print('Valor R$ ' + str(round(latas,0) * 80))

print('\n')
print('Para galões de 3,6L ')
if litrosDeTinta % 3.6 != 0 :
    galao += 1;
    print('Quantidade de galões 3.6L: ' + str(round(galao,0)))
    print('Valor R$ ' + str(round(galao,0) * 25))
print('\n')
print('Para menor desperdício de tinta:')
if litrosDeTinta > 10.8 and litrosDeTinta < 18:
    print('Quantidade de tinta ' + str(litrosDeTinta) + ' comprar uma lata  de 18 litros valor de R$80,00.')
elif litrosDeTinta <= 10.8:
    galoes = litrosDeTinta/3.6
    resto = litrosDeTinta % 3.6
    if resto != 0:
        galoes += 1
        print('Quantidade de galo~es 3.6L: ' + str(round(galao,0)))
        print('Valor R$ ' + str(round(galao,0) * 25))
    else:
        print('Quantidade de galo~es 3.6L: ' + str(round(galao,0)))
        print('Valor R$ ' + str(round(galao,0) * 25))
elif litrosDeTinta > 18:
    latas = litrosDeTinta / 18
    resto = litrosDeTinta % 18
    if resto > 10.8:
        latas +=1
        print('Quantidade de latas 18L: ' + str(round(latas,0)))
        print('Valor R$ ' + str(round(latas,0) * 80))
    elif resto < 10.8:
        galoes = litrosDeTinta/3.6
    resto = litrosDeTinta % 3.6
    if resto != 0:
        galoes += 1
        print('Quantidade de galo~es 3.6L: ' + str(round(galao,0)))
        print('Valor R$ ' + str(round(galao,0) * 25))
    else:
        print('Quantidade de galo~es 3.6L: ' + str(round(galao,0)))
        print('Valor R$ ' + str(round(galao,0) * 25))