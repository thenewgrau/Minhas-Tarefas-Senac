import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex04 import Ui_MainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.player = QMediaPlayer(self)

        self.ui.pushButton.clicked.connect(lambda: self.tocarMusica('musica1.mp3'))
        self.ui.pushButton_2.clicked.connect(lambda: self.tocarMusica('musica2.mp3'))
        self.ui.pushButton_3.clicked.connect(lambda: self.tocarMusica('musica3.mp3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.tocarMusica('musica4.mp3'))
        self.ui.pushButton_5.clicked.connect(lambda: self.tocarMusica('musica5.mp3'))
        self.ui.pushButton_6.clicked.connect(self.pararMusica)


    def tocarMusica(self, musica):
        caminhoMusica = os.path.join(os.path.dirname(__file__), 'audios', musica)
        print("Local da música: ", caminhoMusica)

        url = QUrl.fromLocalFile(caminhoMusica)

        if url.isValid():
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            print("Tocando musica...")

        else:
            print("Caminho ou arquivo não identificado... ")

    def pararMusica(self):
        self.player.stop()
        self.isPaused = False
        print("Música parada.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())
