'''Crie uma função que receba dois números como parâmetros e mostre a potência do número 
elevado a n vezes'''

def fun(x,y):
    res = x**y
    print(res)

x = int(input("Digite a base "))
y = int(input("Digite o expoente "))

fun(x,y)