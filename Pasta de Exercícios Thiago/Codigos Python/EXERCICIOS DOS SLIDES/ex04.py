sm = 0
contador = 0
provas = int(input("Digite quantas provas você fez "))
while contador < provas:
    sm = float(input("Quais foram suas notas "))
    contador = contador + 1
media = sm / provas
print(media)
    