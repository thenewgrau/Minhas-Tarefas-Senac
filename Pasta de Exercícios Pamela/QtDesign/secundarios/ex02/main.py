import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ex02 import Ui_MainWindow
from PyQt5.QtCore import QTimer

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dicionario = {
            "1": "Dark Fantasy - Kanye West 4:39",
            "2": "Lovers Rock - TV Girl - 3:53",
            "3": "Juliet - Cavetown - 2:43",
            "4": "Telephones - Vacations 1:44",
            "5": "Sparks - Coldplay - 5:21",
        }

        self.ui.pushButton.clicked.connect(lambda: self.escolherMusica("1"))
        self.ui.pushButton_2.clicked.connect(lambda: self.escolherMusica("2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.escolherMusica("3"))
        self.ui.pushButton_4.clicked.connect(lambda: self.escolherMusica("4"))
        self.ui.pushButton_5.clicked.connect(lambda: self.escolherMusica("5"))

    def escolherMusica(self, musica):
        musicaEscolhida =  self.dicionario.get(musica)
        if musicaEscolhida is not None:
            self.ui.label_7.setText(f"Tocando: {musicaEscolhida}")
            QTimer.singleShot(5000, self.ui.label_7.clear)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())
