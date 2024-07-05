notas = []
nauquero = []
soma = 0
terminar = True

while terminar == True:
    
    print("Diga suas notas rapaizinho ")
    nda = float(input())
    if nda > 10:
        nauquero.append(nda)
    else:
        notas.append(nda)
        soma = sum(notas)
    if nda < 0 or nda >= 10:
        print("Valor invalido !")
        print(f"A sua média aritmética é {soma/len(notas)}") 
        terminar = False