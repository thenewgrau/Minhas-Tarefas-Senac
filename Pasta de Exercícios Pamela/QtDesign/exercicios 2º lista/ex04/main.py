import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ex04 import Ui_MainWindow

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calculadoraAmbulante)

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

    def calculadoraAmbulante(self):
        try:
            num = float(self.ui.lineEdit.text())  
            hrs = float(self.ui.lineEdit_2.text())  
            calculo = num * hrs
            calculoFinal = calculo * 30
            self.ui.label_2.setText(f"R$ {calculoFinal:.2f}")
        except ValueError:
            self.ui.label_2.setText("Precisa ter algum número ai né")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())
    
