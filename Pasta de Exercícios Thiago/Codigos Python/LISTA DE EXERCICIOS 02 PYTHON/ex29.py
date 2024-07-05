idade = int(input("Qual a sua idade ? "))
qntt = int(input("Quanto tempo você trabalhou ? "))
if idade >= 65:
    print("Você pode se aposentar")
elif qntt >= 30:
    print("Você pode se aposentar")
elif idade >= 60 and qntt >= 25:
    print("Você pode se aposentar")
else:
    print("Você não pode se aposentar")