# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

n = float(input('Digite um número:'))

# função is_integer()verifica se o número é inteiro
r = n.is_integer()

if r:
    print('Inteiro')
else:
    print('false')