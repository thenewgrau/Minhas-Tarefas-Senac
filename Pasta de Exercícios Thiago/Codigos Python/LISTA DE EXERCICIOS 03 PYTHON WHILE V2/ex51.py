Joao = []
Jose = []
Felipe = []
Walter = []
nulo = []
branco = []
total = []

while True:
    print("1 para João")
    print("2 para José")
    print("3 para Felipe")
    print("4 para Walter")
    x = int(input())

    if x == 0:
        break

    elif x == 1:
        Joao.append(1)
        total.append(1)
        print("Voto computado !")

    elif x == 2:
        Jose.append(1)
        total.append(1)
        print("Voto computado !")

    elif x == 3:
        Felipe.append(1)
        total.append(1)
        print("Voto computado !")

    elif x == 4:
        Walter.append(1)
        total.append(1)
        print("Voto computado !")

    elif x == 5:
        nulo.append(1)
        total.append(1)
        print("Voto computado !")

    elif x == 6:
        branco.append(1)
        total.append(1)
        print("Voto computado !")

    else:
        print("Votos Joao:",sum(Joao))
        print("Votos Jose:",sum(Jose))
        print("Votos Felipe:",sum(Felipe))
        print("Votos Walter:",sum(Walter))
        print("Percentual de votos nulos sobre total de votos", (sum(total))/(0.01*sum(nulo)),"%")
        

