lst = []
terminar = True
while terminar == True:
    
    print("Digite um número")
    num = int(input())
    lst.append(num)

    if num < 0:
        print("Fim")
        terminar = False

print("Máximo :",max(lst))
print("Minímo :",min(lst))