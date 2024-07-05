'''Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de 
retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.'''

def fun(num):
    if num == 0:
        print("0")
    elif num < 0:
        print("-1")
    else:
        print(1)

num = int(input("Digite o número "))

fun(num)