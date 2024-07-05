lit = []
litn = []
terminar = True
while terminar == True:
    a  = int(input("Digite os números e se quiser encerrar digite o número 0. "))
    if a == 0:
        terminar = False
    if a > 0:
        lit.append(a)
    elif a < 0:
        litn.append(a)
print(f"Numeros positivos : {lit}")
print(f"Numeros negativos : {litn}")