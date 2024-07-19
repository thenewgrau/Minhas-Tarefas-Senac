i = 1
soma = 0

while i < 10:
    try:
        print("Digite um número ")
        x = int(input())
        soma += x
        i += 1

    except:
        print("Digite um valor válido !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

print(f"TOTAL : {soma}")