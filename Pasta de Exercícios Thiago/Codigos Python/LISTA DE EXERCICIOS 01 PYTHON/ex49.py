qlata = int(input("Digite quantas latas de 350ml você quer comprar "))
qgarrafapeq = int(input("Digite quantas garrafas 600ml você quer comprar "))
qgarrafagra = int(input("Digite quantas garrafas 2L você quer comprar "))

lata = qlata * 0.35
garrafapeq = qgarrafapeq * 0.6
garrafagra = qgarrafagra * 2

litros = lata + garrafapeq + garrafagra
print(f"Você vai comprar {litros} litros de refrigerante Frutaba !")