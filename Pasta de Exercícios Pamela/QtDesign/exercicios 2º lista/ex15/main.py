import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ex15 import Ui_MainWindow

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lista = []
        self.i = 0
        self.ui.pushButton.clicked.connect(self.mostrarCaracteres)

        self.ui.actionNovo.triggered.connect(self.novo_arquivo)
        self.ui.actionAbrir.triggered.connect(self.abrir_arquivo)
        self.ui.actionSalvar.triggered.connect(self.salvar_arquivo)
        self.ui.actionSair.triggered.connect(self.sair)

    def novo_arquivo(self):
        self.ui.lineEdit.clear()
        self.ui.label_2.clear()

    def abrir_arquivo(self):
        caminho = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, "r", encoding='utf-8') as f:
                self.ui.textEdit.setText(f.read())

    def salvar_arquivo(self):
        caminho = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(self.ui.textEdit.toPlainText())

    def sair(self):
        self.close()

    
    def mostrarCaracteres(self):
        try:
            letras = str(self.ui.textEdit.toPlainText()).strip()
            letras2 = str(self.ui.textEdit_2.toPlainText()).strip()

            if letras  == letras2:
                self.ui.label_2.setText("Elas são iguais")
            elif len(letras) == len(letras2):
                self.ui.label_2.setText("Possuem o mesmo tamanho")
            elif letras != letras2 and len(letras) != len(letras2):
                self.ui.label_2.setText("Elas não tem nada de igual")
            elif letras == letras2 and len(letras) == len(letras2):
                self.ui.label_2.setText("Elas são do mesmo tamanho e são a mesma coisa parabéns ai.")
            else:
                self.ui.label_2.setText("Não sei como você fez pra ter esse print mas conseguiu parabens")


        except ValueError:
            self.ui.label_4.setText("Precisa ter algum número ai né") 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())