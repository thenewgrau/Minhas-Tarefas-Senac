vetor = []
print("Digite a palavra com 10 caracteres")
rima = str(input())
for i in range(10):
    if rima[i] != "a" and rima[i] != "e" and rima[i] != "i" and rima[i] != "o" and rima[i] != "u":

        vetor.append(rima[i])

print(f"Quantidade de consoantes : {len(vetor)}")
print(vetor)