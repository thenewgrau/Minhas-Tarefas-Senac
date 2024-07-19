class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def getNome(self):
        print(f"Nome do livro: {self.nome}")

    def getAutor(self):
        print(f"Autor: {self.autor}")

    def getEditora(self):
        print(f"Editora: {self.editora}")

    def listarqtdePaginas(self):
        print(f"Páginas: {self.paginas}")

    def setEditora(self,alterarEditora):
        self.editora = alterarEditora
        
