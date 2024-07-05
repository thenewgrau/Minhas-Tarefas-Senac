nota = []
cnt = 0
while cnt <= 7:
    print("Diga seu nome ")
    nome = input()
    print("Qual foi sua nota ")
    x = float(input())
    nota.append(x)

    for i in nota:
        print(f"{cnt+1} Nota = ",i)
    




