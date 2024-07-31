class CarrinhodeCompras:
    def __init__(self):
        self.produtos = []

    def inserirProduto(self, produto):
        self.produtos.append(produto)

    def listarProduto(self):
        for prod in self.produtos:
            print(f'{prod.nome} \nPreço R${prod.preco:.2f}')

    def getSoma(self):
        total = 