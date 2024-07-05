lista = []
lista_pares = []
listaglobal = []

while True:
    print("Digite o número")
    x = int(input())

    if x == 0:
        print("Finalizado.")
        break
    
    elif x % 2 == 0:
        lista_pares.append(x)
        listaglobal.append(x)
    else:
        lista.append(x)
        listaglobal.append(x)

print(f"Quantidade de números digitados : {len(lista)+len(lista_pares)}")
print(f"Soma de todos : {sum(lista)+sum(lista_pares)}")
print(f"Soma dos Pares : {sum(lista_pares)}")
print(f"Média : {((sum(lista)+sum(lista_pares)))/(len(lista)+len(lista_pares))}")
print(f"Média Pares : {sum(lista_pares)/len(lista_pares)}")
print(f"Maior número digitado : {max(listaglobal)}")
print(f"Menor número digitado : {min(listaglobal)}")
