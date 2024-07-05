div = []
somas = []
somat = 0
primos =[]
soma = 0
print("Digite seu número inteiro não negativo.")
num = int(input())
if num < 0:
    print("digite um número inteiro positivo !")
else:   
    f = 1
    for i in range(num):
        if num % f == 0:
            somas.append(f)
            f += 1
        else:
            f += 1
if len(div)<2:
    soma += i

print(soma)