# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('Digite M para matutino')
print('Digite V para vespertino')
print('Digite N para noturno')
t = str(input('Qual turno você estuda:'))

if t == 'M':
    print('Bom dia!')
elif t == 'V':
    print('Boa tarde!')
elif t == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')