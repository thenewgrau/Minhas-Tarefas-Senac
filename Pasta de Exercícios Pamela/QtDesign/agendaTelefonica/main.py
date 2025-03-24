import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.uic import loadUi

telaCadastrar = "adicionar.ui"
telaExibir = "tabelaUsuarios.ui"


class TelaCadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(telaCadastrar, self)

        self.usuario = self.carregarUsuarios()

        self.adicionarBotao.clicked.connect(self.salvarUsuario)
        self.listarBotao.clicked.connect(self.abrirListagem)

    def carregarUsuarios(self):
        try:
            with open("usuarios.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def salvarUsuario(self):
        nome = self.nomeInput.text()
        telefone = self.numInput.text()

        if not nome or not telefone:
            QMessageBox.warning(self, "Erro", "Os campos Nome e Telefone são obrigatórios!")
            return

        user = {
            "nome": nome,
            "telefone": telefone,
        }

        self.usuario.append(user)

        with open("usuarios.json", "w") as f:
            json.dump(self.usuario, f, indent=4)

        QMessageBox.information(self, "Sucesso", "Usuario salvo com sucesso!")

        self.nomeInput.clear()
        self.numInput.clear()

    def abrirListagem(self):
        self.hide()
        self.telaListagem = TelaListagem(self.usuario, self)
        self.telaListagem.show()

class TelaListagem(QMainWindow):
    def __init__(self, usuario, telaCadastro):
        super().__init__()
        loadUi(telaExibir, self)

        self.telaCadastro = telaCadastro
        self.usuario = usuario 

        self.tabelaUsuarios.setColumnCount(2)
        self.tabelaUsuarios.setHorizontalHeaderLabels(["Nome", "Telefone"])

        self.botaoVoltar.clicked.connect(self.voltarCadastro)
        self.botaoRemover.clicked.connect(self.excluirUsuario)
        self.botaoEditar.clicked.connect(self.editarUsuario)

        self.carregarUsuario()

    def carregarUsuario(self):
        if not self.usuario:
            QMessageBox.warning(self, "Erro", "Nenhum usuário encontrado!")
            return
        
        self.tabelaUsuarios.setRowCount(0)

        for user in self.usuario:
            row = self.tabelaUsuarios.rowCount()
            self.tabelaUsuarios.insertRow(row)

            self.tabelaUsuarios.setItem(row, 0, QTableWidgetItem(user["nome"]))
            self.tabelaUsuarios.setItem(row, 1, QTableWidgetItem(user["telefone"]))

    def editarUsuario(self):
        linha = self.tabelaUsuarios.currentRow()
        
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione um usuário para editar!")
            return
        
        nome_atual = self.tabelaUsuarios.item(linha, 0).text()
        telefone_atual = self.tabelaUsuarios.item(linha, 1).text()

        nome, ok_nome = QInputDialog.getText(self, "Editar Nome", "Digite o novo nome:", text=nome_atual)
        telefone, ok_telefone = QInputDialog.getText(self, "Editar Telefone", "Digite o novo telefone:", text=telefone_atual)

        if ok_nome and ok_telefone:
            self.usuario[linha]["nome"] = nome
            self.usuario[linha]["telefone"] = telefone

            with open("usuarios.json", "w") as f:
                json.dump(self.usuario, f, indent=4)

            self.tabelaUsuarios.setItem(linha, 0, QTableWidgetItem(nome))
            self.tabelaUsuarios.setItem(linha, 1, QTableWidgetItem(telefone))

            QMessageBox.information(self, "Sucesso", "Usuário editado com sucesso!")

    def excluirUsuario(self):
        linha = self.tabelaUsuarios.currentRow()
        
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione um usuário para excluir!")
            return
        
        resposta = QMessageBox.question(self, "Excluir", "Tem certeza que deseja excluir este usuário?", 
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if resposta == QMessageBox.Yes:
            del self.usuario[linha]

            with open("usuarios.json", "w") as f:
                json.dump(self.usuario, f, indent=4)

            self.tabelaUsuarios.removeRow(linha)

            QMessageBox.information(self, "Sucesso", "Usuário excluído com sucesso!")
                    

    def voltarCadastro(self):
        self.hide()
        self.telaCadastro.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaCadastro()
    window.show()
    sys.exit(app.exec_())

# OBS: usei chatgpt, tem coisa ai que eu não sabia como fazer...