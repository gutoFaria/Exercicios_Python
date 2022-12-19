# Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:
# e. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# f. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# g. A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = float(input('Digite a nota do aluno:'))
n2 = float(input('Digite a nota do aluno:'))
n3 = float(input('Digite a nota do aluno:'))

m = (n1+n2+n3)/3

if m >=7 and m < 10:
    print('Aprovado \nmédia = ' + str(round(m,2)))
elif m < 7:
    print('Reprovado \nmédia = ' + str(round(m,2)))
elif m == 10:
    print('Aprovado com Distinção \nmédia = 10')