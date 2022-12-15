# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
# aproximado de download do arquivo usando este link (em minutos).

mb = float(input('Digite o tamanho do arquivo em MB:'))
vel = float(input('Digite a velocidade do link de internet:'))
tempo = mb / vel

tempo /= 60

print('Velocidade de download do arquivo de ' + str(round(tempo,0))+ ' minuto')