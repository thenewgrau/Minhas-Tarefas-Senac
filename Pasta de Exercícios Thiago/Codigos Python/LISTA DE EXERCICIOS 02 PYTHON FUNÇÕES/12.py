'''Elabore uma função que receba a distância em Km e a quantidade de litros de gasolina 
consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma 
mensagem de acordo com a tabela abaixo'''

def calc(km,l):
    consumo = km / l
    
    if consumo <= 8:
        print("Gasta muito!")
        print(f"Gastou : {consumo} L")

    elif consumo > 8 and consumo <= 15:
        print("Econômico!")
        print(f"Gastou : {consumo} L")

    else:
        print("Super Econômico!")
        print(f"Gastou : {consumo} L")

print("Digite a distância")
km = int(input())
print("Digite os litros gastos")
l = int(input())

calc(km,l)