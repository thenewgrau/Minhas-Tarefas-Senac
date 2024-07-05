'''
crie uma lista com 6 números inteiros 
adicione na lista 6 números decimais
remova os dois ultimos itens da lista adicione 10 e 11 na posição 1 e 2 da lista
imprima o maior número da lista
imprima o menor numero da lista
imprima a soma dos itens da lista
imprima a media dos itens dos itens da lista
remova o numero 10 e imprima o indice 11
multiplique o quinto pelo sexto elemento da lista
imprima a lista em ordem decrescente
'''
lista = [1 ,2 ,3 ,4 ,5, 6]
listadois = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
listat = lista + listadois
listat.pop(-1)
listat.pop(-1)
listat.insert(1, 10)
listat.insert(2, 11)
print(listat)
print("Maximo :",max(listat))
print("Minimo :",min(listat))
print("Soma :",sum(listat))
print("Média :",round(sum(listat)/len(listat),2))
listat.remove(10)
print(listat)
print(listat.index(11))
print(listat[9]*listat[10])
print(sorted(lista,reverse=True))