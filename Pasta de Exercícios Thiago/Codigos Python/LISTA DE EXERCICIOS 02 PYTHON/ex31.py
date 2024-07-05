km = float(input("Quantos Km você andou com seu carro ? "))
litr = float(input("Quantos litros foram consumidos ? "))

kml = km / litr

if kml < 8:
    print("Venda o carro!")
elif kml > 8 and kml < 11:
    print("Econômico!")
elif kml > 12:
    print("Super econômico!") 