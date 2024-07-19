def fun(*args):
    for i,it in enumerate(args):
        print(i+1, it)

res = fun('Pera','Uva','Maça','Salada mista')
print(res)