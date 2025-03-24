import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from telaFotoMostrar import Ui_MainWindow
 
class MinhaJanela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.ui.pushButton.clicked.connect(self.abrirImagem)
 
    def abrirImagem(self):
        image_path = 'C:/Users/EduardoDutras/Downloads/QtDesign/2403/ex02/paraguai.png'
        pixmap = QPixmap(image_path)


        if pixmap.isNull():
            print("Não tem foto irm")

        else:
            print("Sucesso!")
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)
       
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())