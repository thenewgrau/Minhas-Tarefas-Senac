'''O gestor de uma rede de shoppings, precisa contratar um
sistema para administrar o estacionamento, a principal função do
sistema é calcularTempo(). Considere o valor mínimo de R$9,00
por hora e R$ 1,50 por hora adicional. O principal argumento da
função é o tempo utilizado em minutos, a função deve retornar o
valor total. Caso o usuário fique no estacionamento por menos de
15 minutos, o tempo utilizado não será cobrado.
'''

def calcularTempo(min):
    if min <= 15:
        valores = 0

    else:
        horas = min / 60

        if horas < 1:
            valores = 9

        else:
            horas -= 1
            valores = horas * 1.5 + 9
    
    print(f"{min} minutos, o valor do estacionamento fica R${valores:.2f}")
    
calcularTempo(14)
calcularTempo(240)
