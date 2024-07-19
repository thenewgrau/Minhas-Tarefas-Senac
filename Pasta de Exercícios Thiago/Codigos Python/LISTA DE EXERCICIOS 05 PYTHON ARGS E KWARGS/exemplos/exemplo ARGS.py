### *ARGS É UMA LISTA DE PARAMETROS

def mult(*args):
    soma = 0
    i = 0
    while i < len(args):
        soma += args[i]
        i += 1
    return soma

res = mult(3,4,3,2,3,68,8,7,5)
print(res)