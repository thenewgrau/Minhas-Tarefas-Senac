def fun(*args):
    soma = 0
    i = 0
    while i < len(args):
        soma += args[i]
        i += 1
    
    print(f"Soma : {soma}")

fun(3.5,6.5,9.5)