idade = []
zero = []
terminar = 1


while terminar == 1:

    escida = int(input("Digite sua idade "))
    idade.append(escida)

    if escida == 0:
        zero.append(escida)
        idade.remove(idade[-1])
        terminar = 0

        print(f"A idade média desse grupo é {sum(idade)/len(idade)}")