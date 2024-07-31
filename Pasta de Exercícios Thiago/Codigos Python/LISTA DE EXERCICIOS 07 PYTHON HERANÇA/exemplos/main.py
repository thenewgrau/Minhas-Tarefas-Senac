from Produto import Produto
from Carrinho import CarrinhodeCompras


car = CarrinhodeCompras()
    
p1 = Produto('Iphone 15', 9999, 999)
p2 = Produto('Notebook Asus', 1999, 12)
p3 = Produto('Camisa do Santos', 1334, 9981)

car.inserirProduto(p1)
car.inserirProduto(p2)
car.inserirProduto(p3)

car.listarProduto()