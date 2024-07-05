precoat = float(input("Digite o preço do seu produto "))
if precoat <= 50:
    precoatu = precoat * 0.05
    precoatu = precoatu + precoat
    print(f"O percentual de aumento do seu produto é {precoatu}")
else:
    if precoat >= 50 and precoat <=100:
        precoatu = precoat * 0.10
        precoatu = precoatu + precoat
        print(f"O aumento do seu produto é {precoatu}.")
    elif precoat > 100:
        precoatu = precoat * 0.15
        precoatu = precoatu + precoat
        print(f"O percentual atualizado do seu produto é {precoatu}")