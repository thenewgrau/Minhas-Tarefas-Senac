def fun(*args):
    soma = 0
    i = 0
    while i < len(args):
        soma += args[i]
        i += 1

    res = soma / len(args)
    return res

e = fun(6,6,6,6)
print(f"Média : {e}")