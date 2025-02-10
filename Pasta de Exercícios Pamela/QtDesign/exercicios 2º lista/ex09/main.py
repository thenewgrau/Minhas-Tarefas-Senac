import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ex09 import Ui_MainWindow

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

            letraInsana = str(self.ui.lineEdit.text())
            if letraInsana == "M" or letraInsana == "m":
                self.ui.label_2.setText("Bom dia")
                self.ui.lineEdit.clear()
            elif letraInsana == "V" or letraInsana == "v":
                self.ui.label_2.setText("Boa tarde")
                self.ui.lineEdit.clear()
            elif letraInsana == "N" or letraInsana == "n":
                self.ui.label_2.setText("Boa noite")
                self.ui.lineEdit.clear()
            else:
                self.ui.label_2.setText("Leia as regras poxa..")
                self.ui.lineEdit.clear()


            
        except ValueError:
            self.ui.label_2.setText("Leia as regras poxa..")

            #to com preguiça de tirar o try e except professora desculpa, eu sei que não tem necessidade, se bem que no tempo que eu digitei isso eu podia ter tirado 
           

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())
    
