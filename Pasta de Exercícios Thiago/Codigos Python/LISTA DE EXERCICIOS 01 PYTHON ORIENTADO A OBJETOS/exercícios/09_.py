'''Adicione na função calcularTempo() do sistema para
estacionamento o valor dos impostos pago pelo cliente. Considere
o PIS: 0,33% , COFINS: 0,20% e ICMS: 17% no valor e imprima o
recibo do cliente de acordo com a saída abaixo:'''

def calcularTempo(min,pis,cofins,icms):
    if min <= 15:
        valores = 0

    else:
        horas = min / 60
        
        if horas < 1:
            valores = 9

        else:
            horas -= 1
            valores = horas * 1.5 + 9
            pis = valores * 0.033
            cofins = valores * 0.020
            icms = valores * 0.17
    print(f"TEMPO: {min / 60} horas")
    print(f"PIS: R$ {pis:.2f}")
    print(f"COFINS: R$ {cofins:.2f}")
    print(f"ICMS: R$ {icms:.2f}" )
    print(f"IMPOSTOS: R$ {pis+cofins+icms:.2f}")
    print(f"TOTAL: R$ {valores:.2f}")
    
calcularTempo(240,0,0,0)