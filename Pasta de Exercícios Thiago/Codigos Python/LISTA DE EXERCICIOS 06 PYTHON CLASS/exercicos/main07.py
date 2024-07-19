from Ex07 import Triangulo

print("Digite o lado A")
la = int(input())
print("Digite lado B")
lb = int(input())
print("Digite lado C")
lc = int(input())

tri = Triangulo(la,lb,lc)

tri.calcPerimetro()
tri.getMlado()
tri.Medidas()