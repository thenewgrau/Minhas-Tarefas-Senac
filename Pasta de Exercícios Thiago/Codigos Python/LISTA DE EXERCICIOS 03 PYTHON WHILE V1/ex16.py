n = int(input("Digite o valor de n "))
contador = 1
if n // 2 != 0:
    while contador < n:
        contador += 2
        print(contador)
elif n == 1:
    print("1")
else:
    print("DIGITE UM VALOR CORRETO ADERBAL")