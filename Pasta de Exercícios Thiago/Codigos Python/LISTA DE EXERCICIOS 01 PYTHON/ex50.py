import math
w = float(input("digite o primeiro valor para W "))
x = float(input("Digite o segundo valor para X "))
y = float(input("Digite o terceiro valor para Y "))
z = float(input("Digite o quarto e ultimo valor para Z "))

d = math.sqrt((w - x)**2 + (y - z)**2)

if(d >= 10):
    print("Você está longe da saida")
else:
    print("Perto")