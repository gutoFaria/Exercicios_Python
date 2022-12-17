# Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, que depende 
# do salário bruto (conforme tabela abaixo) e 3% para o Sindicato 
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# • Desconto do IR:
# • Salário Bruto até 900 (inclusive) - isento
# • Salário Bruto até 1500 (inclusive) - desconto de 5%
# • Salário Bruto até 2500 (inclusive) - desconto de 10%
# • Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade 
# de hora é 220. Salário Bruto: (5 * 220) : R$ 1100,00 (-) IR (5%) : R$ 55,00 (-) 
# INSS ( 10%) : R$ 110,00 FGTS (11%) : R$ 121,00 Total de descontos : R$ 165,00 Salário Liquido : R$ 935,00

h = float(input('Digite a quantidade de horas trabalhadas'))
s = float(input('Digite o valor da hora trabalhada'))

sb = s * h
fgts = sb * 0.11
ir = sb * 0.05
inss = sb * 0.1
sin = sb * 0.03

sl = sb - (ir + inss + sin)

if sb <= 900:
    print('Salário bruto R$ ' + str(round(sb,2)))
    print('FGTS R$: ' + str(round(fgts,2)))
    print('IR R$: ' + str(round(ir,2)))
    print('INSS R$: ' + str(round(inss,2)))
    print('Sindicato R$: ' + str(round(sin,2)))
    print('Salário líquido R$ ' + str(round(sl,2)))
elif sb > 900 and sb <= 1500:
    des = sb * 0.05
    sl = sb - (ir + inss + sin + des)
    print('Salário bruto R$ ' + str(round(sb,2)))
    print('FGTS R$: ' + str(round(fgts,2)))
    print('IR R$: ' + str(round(ir,2)))
    print('INSS R$: ' + str(round(inss,2)))
    print('Sindicato R$: ' + str(round(sin,2)))
    print('Desconto R$: ' + str(round(des,2)))
    print('Salário líquido R$ ' + str(round(sl,2)))
elif sb > 1500 and sb <= 2500:
    des = sb * 0.1
    sl = sb - (ir + inss + sin + des)
    print('Salário bruto R$ ' + str(round(sb,2)))
    print('FGTS R$: ' + str(round(fgts,2)))
    print('IR R$: ' + str(round(ir,2)))
    print('INSS R$: ' + str(round(inss,2)))
    print('Sindicato R$: ' + str(round(sin,2)))
    print('Desconto R$: ' + str(round(des,2)))
    print('Salário líquido R$ ' + str(round(sl,2)))
elif sb > 2500:
    des = sb * 0.2
    sl = sb - (ir + inss + sin + des)
    print('Salário bruto R$ ' + str(round(sb,2)))
    print('FGTS R$: ' + str(round(fgts,2)))
    print('IR R$: ' + str(round(ir,2)))
    print('INSS R$: ' + str(round(inss,2)))
    print('Sindicato R$: ' + str(round(sin,2)))
    print('Desconto R$: ' + str(round(des,2)))
    print('Salário líquido R$ ' + str(round(sl,2)))


    