notalab = float(input("Digite a sua nota de lab "))
notasemes = float(input("Digite a sua nota semestral "))
notaexa = float(input("Digite a sua nota de exame final "))

soma = ((notalab*2)+(notasemes*3)+(notaexa*5)/10)

print(soma)
if soma <= 2.9:
    print("Reprovado!")
else:
    if soma >= 3 and soma <= 5.9:
        print("Recuperação")
    else:
        print("Aprovado!")