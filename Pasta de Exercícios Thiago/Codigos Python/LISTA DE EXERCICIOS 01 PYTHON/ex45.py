p = 35
m = 45
g = 55

qntp = int(input("Digite quantas camisetas P você quer "))
qntm = int(input("Digite quantas camisetas M você quer "))
qntg = int(input("Digite quantas camisetas G você quer "))

qntp = float(qntp * p)
qntm = float(qntm * m)
qntg = float(qntg * g)
total = float(qntp + qntm + qntg)
print(f"Você vai pagar R${qntp}, em camisas pequenas. \nVocê também terá que pagar R${qntm}, nas camisas médias \nE por fim terá que pagar também R${qntg} em camisas grandes. \nDando no total R${total}.\n                    Obrigado por comprar conosco!")