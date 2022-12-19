a = 10

def CelsiusParaFahrenheit():
    v = float(input('\tDigite o Valor da temperatura:'))
    f = (9/5*v) + 32
    print('\tCelsius = ' + str(round(v,2)) + '    Fahrenheit = ' + str(round(f,2))) 

def FahrenheitparaCelsius():
    v = float(input('\tDigite o Valor da temperatura:'))
    c = (v-32) * (5/9)
    print('\tFahrenheit = ' + str(round(v,2)) + '    Celsius = ' + str(round(c,2))) 


while a != 0:
    print('\tCONVERSOR DE TEMPERATURA CELSIUS E FAHRENHEIT')
    print('\tDigite [1] para converter Celsius para FAHRENHEIT')
    print('\tDigite [2] para conveter FAHRENHEIT para Celsius')
    print('\tDigite [0] para sair do programa')
    a = int(input('\tEscolha:'))
    
    if a == 1:
        CelsiusParaFahrenheit()
    elif a == 2:
        FahrenheitparaCelsius()
    elif a == 0:
        print('\tSaindo do programa!')
    else:
        print('\tValor inválido!')