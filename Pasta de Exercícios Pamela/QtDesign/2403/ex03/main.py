import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from telaIdadeDiferente import Ui_MainWindow
 
class MinhaJanela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.ui.pushButton.clicked.connect(self.abrirImagem)
 
    def abrirImagem(self):
        idade = int(self.ui.lineEdit.text())

        if idade <= 3:
            image_path = 'C:/Users/EduardoDutras/Downloads/QtDesign/2403/ex03/bebe.png'
            pixmap = QPixmap(image_path)
            self.ui.label_3.setText("bebê")
            self.ui.label_2.setPixmap(pixmap)
            self.ui.label_2.setScaledContents(True)
        
        elif idade > 3 and idade <= 11:
            image_path = 'C:/Users/EduardoDutras/Downloads/QtDesign/2403/ex03/crianca.png'
            pixmap = QPixmap(image_path)
            self.ui.label_3.setText("criança")
            self.ui.label_2.setPixmap(pixmap)
            self.ui.label_2.setScaledContents(True)
        
        elif idade > 11 and idade <= 18:
            image_path = 'C:/Users/EduardoDutras/Downloads/QtDesign/2403/ex03/adolescente.png'
            pixmap = QPixmap(image_path)
            self.ui.label_3.setText("adolescente")
            self.ui.label_2.setPixmap(pixmap)
            self.ui.label_2.setScaledContents(True)

        elif idade > 18 and idade <=60:
            image_path = 'C:/Users/EduardoDutras/Downloads/QtDesign/2403/ex03/adulto.png'
            pixmap = QPixmap(image_path)
            self.ui.label_3.setText("adulto")
            self.ui.label_2.setPixmap(pixmap)
            self.ui.label_2.setScaledContents(True)

        elif idade > 60:
            image_path = 'C:/Users/EduardoDutras/Downloads/QtDesign/2403/ex03/idoso.png'
            pixmap = QPixmap(image_path)
            self.ui.label_3.setText("idoso")
            self.ui.label_2.setPixmap(pixmap)
            self.ui.label_2.setScaledContents(True)
       
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())