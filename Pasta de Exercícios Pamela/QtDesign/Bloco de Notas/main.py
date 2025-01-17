import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from brocoNotas123 import Ui_MainWindow

class editorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNovo.triggered.connect(self.novo_arquivo)
        self.ui.actionAbrir.triggered.connect(self.abrir_arquivo)
        self.ui.actionSalvar.triggered.connect(self.salvar_arquivo)
        self.ui.actionSair.triggered.connect(self.sair)

    def novo_arquivo(self):
        self.ui.textEdit.clear()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = editorTexto()
    window.show()
    sys.exit(app.exec_())
    