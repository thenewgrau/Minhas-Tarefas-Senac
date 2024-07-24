def energ(potenciaeletrica,tempo):
    kwh = potenciaeletrica * tempo
    return kwh

def valorcontaenergia(energ,valorkwh):
    conta = energ * valorkwh
    return conta


res = energ(150,120)

print(f"O consumo foi de {res} KWH")
print(f"O valor da conta foi R${valorcontaenergia(res,13.84)}")

