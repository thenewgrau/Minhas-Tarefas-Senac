pessoas = int(input("Quantas pessoas querem entrar no elevador ? "))
peso = int(input("Qual é a soma do peso delas ? "))

if(pessoas > 5 or peso > 350):
    print("Limite de carga excedido!")
else:
    print("subindo!!")
