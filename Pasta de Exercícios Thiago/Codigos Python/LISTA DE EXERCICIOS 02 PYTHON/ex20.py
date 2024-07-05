notaum = float(input("Digite a sua primeira nota "))
notadois = float(input("Digite a sua segunda nota "))
notatres = float(input("Digite a sua terceira nota "))

soma = (notaum + notadois +(notatres*2) / (1+1+2))

if soma >= 60:
    print("Aprovado")
else:
    print("Reprovado")