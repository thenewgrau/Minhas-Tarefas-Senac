interi = int(input("Digite o inicio do seu intervalo "))
interf =  int(input("Digite o final do seu intervalo "))
soma = 0
if interf < interi:
    print("não podi")
else:
    while interi < interf:
        interi +=2
        soma += interi
        print(interi)

print(soma-interi)
