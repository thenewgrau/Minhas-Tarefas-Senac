cnt = 0
print("Digite o valor de 'a'")
a = int(input())
print("Agora o valor de 'b'")
b = int(input())
for i in range(b,a):
    if i % 2 !=0:
        cnt += 1
        print(i)
        print(f"Contador : {cnt}")