matriz = []

for i in range(3):

    linhas = []
    for i in range(3):
        print("Digite o número")
        x = int(input())
        linhas.append(x)
    matriz.append(linhas)

for i in matriz:
    print(i)