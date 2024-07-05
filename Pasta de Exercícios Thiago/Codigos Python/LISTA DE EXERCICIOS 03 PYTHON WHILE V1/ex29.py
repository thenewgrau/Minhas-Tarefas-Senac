num = int(input("Digite seu número "))
i = 1
for n in range(20):
    if num % i == 0:
        print(i)
        i += 1
    else:
        i += 1 

    