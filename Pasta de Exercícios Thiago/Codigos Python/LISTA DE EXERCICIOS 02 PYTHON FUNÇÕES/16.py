'''Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura. Por exemplo, a 
saída para n = 4 seria:'''

def fun(n):
    for i in range(n+1):
        print("*"*i)
    for x in range(n-1,0,-1):
        print("*"*x)

print("Digite n")
n = int(input())
fun(n)