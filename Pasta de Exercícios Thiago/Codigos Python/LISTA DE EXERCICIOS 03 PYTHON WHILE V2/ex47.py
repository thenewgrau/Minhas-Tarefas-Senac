soma = 0

for i in range(1,11):
    soma  += i**2
    print(soma)

somapri = 0

for n in range(1,11):
    somapri += n
    
somapri = somapri**2
print(somapri)

print(f"A soma do quadrado dos 10 primeiros números é {soma} \nO quadrado da soma dos 10 primeiros números inteiros é {somapri}")
print(f"A diferença deles é : {somapri-soma}")