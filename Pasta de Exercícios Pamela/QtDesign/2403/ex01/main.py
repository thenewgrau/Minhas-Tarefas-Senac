import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from telaContato import Ui_MainWindow
 
class MinhaJanela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.ui.pushButton.clicked.connect(self.abrir_whatsapp)
 
    def abrir_whatsapp(self):
        facebook_link = "https://www.youtube.com/watch?v=doTxaNBy8aY"
        webbrowser.open(facebook_link)
       
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())