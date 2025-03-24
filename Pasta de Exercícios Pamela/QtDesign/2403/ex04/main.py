import sys
import os
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from perfil import Ui_MainWindow
 
class MinhaJanela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.ui.instagram.clicked.connect(self.instagram)
        self.ui.whatsapp.clicked.connect(self.whatsapp)
        self.ui.facebook.clicked.connect(self.facebook)

        image_path = 'C:/Users/EduardoDutras/Downloads/QtDesign/2403/ex04/ronaldinho.png'
        pixmap = QPixmap(image_path)


        if pixmap.isNull():
            print("Não tem foto irm")

        else:
            print("Sucesso!")
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)
    
    def instagram(self):
        facebook_link = "https://www.lojagtsm1.com.br/bicicletas/aro-29/bicicleta-gts-rav-aro-29-freio-hidraulico-quadro-full-suspension-carbono-red-1x12-shimano-xtr?parceiro=4377&variant_id=9699&parceiro=4377&gad_source=1&gclid=Cj0KCQiA1p28BhCBARIsADP9HrNTjbbPHKanisnJtml8THzMYy53BT-79y48oyV8fb68fZSQd5hheAQaAmPbEALw_wcB"
        webbrowser.open(facebook_link)

    def whatsapp(self):
        facebook_link = "https://www.instagram.com/ronaldinhoytb/"
        webbrowser.open(facebook_link)

    def facebook(self):
        facebook_link = "https://www.youtube.com/watch?v=doTxaNBy8aY"
        webbrowser.open(facebook_link)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())