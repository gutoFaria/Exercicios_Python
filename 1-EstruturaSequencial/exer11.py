# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = float(input('Digite o terceiro número: '))

a = (n1*2) * (n2/2);
print('Produto do dobro do primeiro número com a metade do segundo: ' + str(a))
b= float(n1 * 3) + n3
print('Soma do triplo do primeiro com o terceiro: ' + str(round(b,1)))
c=n3**3
print('O terceiro elevado ao cubo: ' + str(round(c,1)))