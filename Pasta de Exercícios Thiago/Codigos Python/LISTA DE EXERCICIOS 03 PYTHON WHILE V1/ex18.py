lista = []
contador = int(input("Digite quantos numeros vc quer "))
qnt = 0
while qnt < contador:
    lista.append(int(input("Digite os números ")))
    qnt += 1
print(max(lista))