x = []
cont = 0
while cont < 10:
    x.append(int(input("Digite os números ")))
    cont = cont + 1
    
print("O maior número entre eles é :", max(x))
print("O menor número entre eles é :", min(x))