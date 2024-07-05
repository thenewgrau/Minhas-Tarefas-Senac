x = int(input("Digite o seu numero: "))
y = 0
if x > 100 and x < 9999:
    x = str(x)
    for i in x:
        print(i)
   
else:
    print("Digite um valor válido!")