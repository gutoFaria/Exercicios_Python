# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois 
# informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# h. Exemplo 1: Para sacar a quantia de 256 reais, 
# o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# i. Exemplo 2: Para sacar a quantia de 399 reais, 
# o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

v = int(input('Qual o valor a ser sacado:'))

#IMCOMPLETO

if v < 10 or v > 600:
    print('Valor para saque incorreto!')
elif v > 100:
    n1 = v / 100 # pega a quantidade de notas de 100
    print(str(round(v/100,0)) + ' notas de cem')
    r = v % 100 # pega o resto da divisão e verifica se é maior que 50
    if r > 50:
        n1 = r / 50
        print(str(round(n1,0)) + ' notas de cinquenta')
        r2 = r % 50
        if r2 > 10:
            n1 = r2 / 10
            print(str(round(n1,0)) + ' notas de dez')
            r3 = r2 % 10
            if r3 > 5:
                n1 = r3 / 5
                print(str(round(n1,0)) + ' notas de cinco')
                r4 = r3 % 5
                if r4 > 0:
                    print(str(round(r4,0)) + ' notas de um')
        elif r2 < 10 and r2 > 5:
            n1 = r2 / 5
            print(str(round(n1,0)) + ' notas de cinco')
            r3 = r2 % 5
            if r3 > 0:
                print(str(round(r3,0)) + ' notas de um')
        elif r2 > 0:
            print(str(round(r2,0)) + ' notas de um')