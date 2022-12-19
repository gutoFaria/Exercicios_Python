# Faça um Programa que leia um número inteiro menor que 1000 
# e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# • Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# • 326 = 3 centenas, 2 dezenas e 6 unidades
# • 12 = 1 dezena e 2 unidades Testar com: 
# 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

n = str(input('Digite um número menor que 1000:'))
l = []



for i in n:
    l.append(i)

#operador ternário 
p1 = 'centena' if l[0] == '1' else 'centenas'
p2 = 'dezena' if l[1] == '1' else 'dezenas'
p3 = 'unidade' if l[2] == '1' else 'unidades'


print(n + ' = ' + l[0] +' '+ p1 +', ' + l[1] + ' '+p2 +' e ' + l[2] + ' ' +p3)
