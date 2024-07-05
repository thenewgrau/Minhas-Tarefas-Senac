numeros = [2,11,4,11,5,9,99,11]
i = -1
contador = 0 
print(len(numeros))
print("*"*50)
while i < len(numeros) - 1:
    i += 1
    if numeros[1] != 11:
        continue
    else:
        print("11 está aqui!")
        contador += 1
print("quantidade de números 11 encontrados :",contador)