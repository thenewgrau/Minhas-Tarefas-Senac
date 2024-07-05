b = 1
d = 1
c = 0
soma = 0
while c < 50:

    b += 2
    d += 1
    c += 1
    soma = float(b/d)
    print(f"{b}/{d} Soma: {soma:.2f}")
    
    if b == 99:
        break
    
    if d == 50:
        break