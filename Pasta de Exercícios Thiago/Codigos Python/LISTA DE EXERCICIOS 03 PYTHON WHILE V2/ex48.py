lst = [1,1,4,5,6,7,3,2,2,-1]
while True:
    print("Digite o número")
    x = int(input())

    if x in lst:
        print(lst.count(x))
    
    else:
        print("Número não listado!")

        