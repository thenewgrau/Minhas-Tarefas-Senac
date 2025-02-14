import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ex01 import Ui_MainWindow
from PyQt5.QtCore import QTimer

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dicionario = {
            "1": 20.21,
            "2": 7.49,
            "3": 17.49,
            "4": 57.12,
            "5": 15.99,
            "6": 10.50,
            "7": 5.31,
            "8": 47.49,
            "9": 7.21,
            "10": 127.49
        }

        self.produtos_selecionados = []

        self.ui.pushButton.clicked.connect(lambda: self.adicionarProduto("1"))
        self.ui.pushButton_2.clicked.connect(lambda: self.adicionarProduto("2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.adicionarProduto("3"))
        self.ui.pushButton_4.clicked.connect(lambda: self.adicionarProduto("4"))
        self.ui.pushButton_5.clicked.connect(lambda: self.adicionarProduto("5"))
        self.ui.pushButton_6.clicked.connect(lambda: self.adicionarProduto("6"))
        self.ui.pushButton_7.clicked.connect(lambda: self.adicionarProduto("7"))
        self.ui.pushButton_8.clicked.connect(lambda: self.adicionarProduto("8"))
        self.ui.pushButton_9.clicked.connect(lambda: self.adicionarProduto("9"))
        self.ui.pushButton_10.clicked.connect(lambda: self.adicionarProduto("10"))

        self.ui.pushButton_11.clicked.connect(self.somarTudo)

    def adicionarProduto(self, chave):
        valor = self.dicionario.get(chave)
        if valor is not None:
            self.produtos_selecionados.append(valor)

    def somarTudo(self):
        total = sum(self.produtos_selecionados)
        self.ui.label_12.setText(f'Total: R${total:.2f}')
        
        QTimer.singleShot(5000, self.ui.label_12.clear)
        self.produtos_selecionados = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())
