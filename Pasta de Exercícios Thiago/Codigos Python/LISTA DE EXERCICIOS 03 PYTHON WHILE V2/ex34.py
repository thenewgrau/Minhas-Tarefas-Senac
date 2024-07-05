vt1 = []
vt2 = []#par
vt3 = []#impar

cnt = 0

while cnt < 20:
    print("Digite o valor")
    num = int(input())
    if num % 2 == 0:
        vt2.append(num)
    elif num % 2 != 0:
        vt3.append(num)
    
    vt1.append(num)
    cnt = cnt + 1
    print("Vetor TODOS: ",vt1)
    print("Vetor Par :",vt2)
    print("Vetor Impar :",vt3)