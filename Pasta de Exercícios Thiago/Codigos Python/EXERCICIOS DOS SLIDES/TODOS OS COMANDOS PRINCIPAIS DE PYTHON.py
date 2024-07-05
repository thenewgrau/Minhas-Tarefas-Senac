numeros = [10,20,30,40,50,60,70,80,90]
num = numeros[4]

# Posição
print("posição :",numeros[2])
print("#"*50)

#  Soma
print("soma mais dificil :",numeros[2]+numeros[5])
print("#"*50)

# Número de componentes
### len()
print("Numero de componentes :",len(numeros))
print("#"*50)

# Entre posições
print("entre posições :",numeros[2:6])
print("#"*50)

# Soma dos componentes
### sum()
print("soma :",sum(numeros))
print("#"*50)

# Número máximo da lista
### max()
print("máximo :",max(numeros))
print("#"*50)

# Número minímo da lista
### min()
print("minimo :",min(numeros))
print("#"*50)

# Adicionar componentes na lista
### numeros.append()
print("Numeros.append :",numeros.append(100))
print("#"*50)

# Remove componente no final da lista
### numeros.pop()
print(f"Remove.pop : {numeros.pop(4)}")
print("#"*50)

# Remove números
### .remove()
numeros.remove(40)
print("Remove :",numeros)
print("#"*50)

# Mostrar o local na lista
### .index 
indice = numeros.index(20)
print(f".index : {indice}")
print("#"*50)

# Adicionar um número em um determinado local
### .insert(posição,numero)
indice = numeros.insert(2,30)
print(f".insert : {indice}")
print("#"*50)

# Ordenar Listas Crescente
### sorted()
numeros1 = [1 ,6 ,2 ,7 ,10 ,3]
numeros2 = [4 ,20 ,80 ,43 ,21 ,23, 34]
numjuntos = numeros1 + numeros2
print("Em ordem crescente :",sorted(numjuntos))
print("#"*50)

# Ordenar Listas Decrescente
### sorted(variavel,reverse=True)
print("Em ordem decrescente :",sorted(numjuntos,reverse=True))
print("#"*50)