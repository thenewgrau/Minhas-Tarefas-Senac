div = []
print("Digite seu número para verificar se é primo ou não")
a = int(input())
f = 1
for i in range(a):
    if a % f == 0:
        div.append(f)
        f += 1
    else:
        f += 1

if len(div) <= 2:
    print("é primo")
else:
    print("não é primo")