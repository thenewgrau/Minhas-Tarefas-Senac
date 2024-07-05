'''Elabore uma função que receba dois números inteiros positivos por parâmetros e retorne a 
soma dos N números inteiros existentes entre eles.'''

def media(a):
    res = ((lst[0]+lst[1]+ lst[2]) / len(lst))
    print(f"Média Aritmética: {res}")

def mediap(p):
    res = ((lst[0]*5+lst[1]*3+lst[2]*2) / 10)
    print(f"Média Poderana: {res}")

lst = []
cnt = 1
while cnt <= 3:
    print(f"Digite sua {cnt}º nota ")
    lst.append(float(input()))
    cnt += 1
print("Agora informe \nA para Média Aritmética  \nP para Média Poderana")
inf = input().upper()
if inf == "A":
    media(inf)
else:
    mediap(inf)