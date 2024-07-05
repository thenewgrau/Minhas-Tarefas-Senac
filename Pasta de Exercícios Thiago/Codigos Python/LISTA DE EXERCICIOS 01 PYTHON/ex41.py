vt = float(input("Digite quando deu o seu valor total : "))

desc = vt * 0.10
pgav = vt - desc
parcela = vt / 3
cmsa = pgav * 0.05
cmsap = vt * 0.05

print(f"Com desconto de 10% é {desc}")
print(f"Parcelado em 3x é {parcela:.2f}")
print(f"A comissão do seu vendedor é 5% e não terá desconto e será cobrado dando no total {cmsa} reias á vista.")
print(f"A comissão do seu vendendor será é de 5% com o desconto e será cobrado {cmsap} reais á mais sobre o valor total parcelado.")
