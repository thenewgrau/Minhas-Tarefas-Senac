import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ex03 import Ui_MainWindow 

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  


        self.ui.pushButton.clicked.connect(self.maior_numero)

        self.ui.actionNovo.triggered.connect(self.novo_arquivo)
        self.ui.actionAbrir.triggered.connect(self.abrir_arquivo)
        self.ui.actionSalva.triggered.connect(self.salvar_arquivo)
        self.ui.actionSair.triggered.connect(self.sair)

    def novo_arquivo(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
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

    def maior_numero(self):
        try:
            num1 = int(self.ui.lineEdit.text())
            num2 = int(self.ui.lineEdit_2.text())
            num3 = int(self.ui.lineEdit_3.text())

            if(num1 > num2 and num1 > num3):
                self.ui.label_2.setText(str(num1))

            elif(num2 > num1 and num2 > num3):
                self.ui.label_2.setText(str(num2))

            else:
                self.ui.label_2.setText(str(num3))   
            
        except ValueError:
            
            self.ui.label_2.setText("Por favor, insira números válidos.")

    def sair(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())
