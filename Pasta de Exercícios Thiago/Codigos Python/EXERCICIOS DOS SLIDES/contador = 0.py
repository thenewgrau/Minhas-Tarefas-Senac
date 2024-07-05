import time
numero = [92, 43,54,65,76,87,98,23,54,2,21,35,43,6,5,1,12,32,4,3,54,623]
i = 0
while i < len(numero):
    if numero[i] == 21:
        print("Encontramos o número")
        break
    else:
        i = i + 1 
time.sleep(5)
print("fim do programa yay!!!"*80000000)
