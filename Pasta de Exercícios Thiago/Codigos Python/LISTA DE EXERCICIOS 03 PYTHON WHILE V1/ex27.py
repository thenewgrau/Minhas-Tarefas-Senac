a = int(input("Digite seu número "))
sla = 1

for i in range(a, 0, -1):
    sla *= i

    print(sla)