import random
terminar = True
numero = int(random.randint(1,100))

while terminar == True:
    print("Digite seu número")
    num = int(input())
    
    if num > numero:
        print("Menor!")
    
    elif num < numero:
        print("Maior!")
    
    elif num == numero:
        print("Correto!!!")
        terminar = False