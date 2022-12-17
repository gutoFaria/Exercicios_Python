# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
# lhe contraram para desenvolver o programa que calculará os reajustes.
# • Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:
# • salários até R$ 280,00 (incluindo) : aumento de 20%
# • salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# • salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# • o salário antes do reajuste;
# • o percentual de aumento aplicado;
# • o valor do aumento;
# • o novo salário, após o aumento.

s = float(input('Digite o seu salário:'))

if s <= 280:
    print('Salário de R$ ' + str(round(s,2)))
    print('Reajuste de 20%')
    print('Valor de reajuste R$' + str(round(s*0.2,2)))
    s = s + (s * 0.2)
    print('Salário reajustado para R$ ' + str(round(s,2)))
elif s > 280 and s < 700:
    print('Salário de R$ ' + str(round(s,2)))
    print('Reajuste de 15%')
    print('Valor de reajuste R$' + str(round(s*0.15,2)))
    s = s + (s * 0.15)
    print('Salário reajustado para R$ ' + str(round(s,2)))
elif s > 700 and s < 1500:
    print('Salário de R$ ' + str(round(s,2)))
    print('Reajuste de 10%')
    print('Valor de reajuste R$' + str(round(s*0.1,2)))
    s = s + (s * 0.1)
    print('Salário reajustado para R$ ' + str(round(s,2)))
elif s > 1500:
    print('Salário de R$ ' + str(round(s,2)))
    print('Reajuste de 5%')
    print('Valor de reajuste R$' + str(round(s*0.05,2)))
    s = s + (s * 0.05)
    print('Salário reajustado para R$ ' + str(round(s,2)))
