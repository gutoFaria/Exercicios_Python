# Faça um programa que lê as duas notas parciais obtidas por um aluno 
# numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
# • Média de Aproveitamento Conceito Entre 9.0 e 10.0 A 
# Entre 7.5 e 9.0 B 
# Entre 6.0 e 7.5 C 
# Entre 4.0 e 6.0 D 
# Entre 4.0 e zero E 
# O algoritmo deve mostrar na tela as notas, a média, 
# o conceito correspondente e a mensagem “APROVADO” 
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

m = (n1+n2) /2

print('Nota 1: '+ str(round(n1,2)))
print('Nota 2: '+ str(round(n2,2)))
print('Média: '+ str(round(m,2)))
print('Conceito do aluno')
if m >=9 and m <= 10:
    print('A')
    print('Aprovado')
elif m >=7.5 and m < 9:
    print('B')
    print('Aprovado')
elif m >= 6 and m < 7.5:
    print('C')
    print('Aprovado')
elif m >= 4 and m < 6:
    print('D')
    print('Reprovado')
elif m > 0 and m < 4:
    print('E')
    print('Reprovado')