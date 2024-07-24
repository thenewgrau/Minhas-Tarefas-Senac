class Brinquedos:
    def __init__(self, nome, cor, tamanho, preco):
        self._nome = nome
        self._cor = cor
        self._tamanho = tamanho
        self._preco = preco

    def queroBrincar(self):
        return print(f"Estou brincando com o {self._nome}, da cor {self._cor}, do tamanho {self._tamanho}, do preco R${self._preco}")
    
class Carrinho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
class Joaninha(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Lego(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Boneca(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Tabuleiro(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class jogoDaVelha(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class quebraCabeca(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class videoGame(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Piao(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Estilingue(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
