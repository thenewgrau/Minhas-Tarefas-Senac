paes = int(input("Digite quantos pães você ira fazer hoje Gauchão "))

queijo = 100

presunto = 50

carne = 100

qpc = queijo + presunto + carne

queijot = (queijo*0.001) * paes
presuntot = (presunto*0.001) * paes
carnet = (carne*0.001)* paes
kg = (qpc * 0.001)* paes


print(f"Você terá que comprar {queijot} kg de queijo no total")
print(f"Você terá que comprar {presuntot} kg de presunto no total")
print(f"Você terá que comprar {carnet} kg de carne no total")
print(f"Você terá que comprar {kg} kg, no total, para fazer {paes} pães, hoje Gauchão.")