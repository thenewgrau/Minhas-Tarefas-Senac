lst_i = []
lst_p = []
imp = int(input("Digite seu valor inicial "))
par = int(input("Digite seu valor final "))

if imp // 2 == 0:
    
    lst_i.append(imp)

else:

    lst_p.append(imp)

if par // 2 == 0:

    lst_p.append(par)

else:

    lst_p.append(par)

cnt = imp + 1

while cnt < par:

    if cnt // 2 == 0:

        lst_p.append(cnt)
        cnt += 1
    
    else:

        lst_i.append(cnt)
        cnt += 1

print(f"A multiplicação dos números impares é igual a : {lst_i}")
print(f"A soma dos pares impares é : {sum(lst_p)}")