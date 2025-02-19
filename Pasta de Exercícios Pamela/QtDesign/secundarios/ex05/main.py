import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex05 import Ui_MainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.player = QMediaPlayer(self)

        self.ui.pushButton.clicked.connect(self.tocarMusica)
        self.ui.pushButton_2.clicked.connect(self.pararMusica)


    def tocarMusica(self):
        
        musicaDele = self.ui.lineEdit.text() 


        if musicaDele == "musica1" or musicaDele == "Musica1":
            caminhoMusica = os.path.join(os.path.dirname(__file__), 'audios', 'musica1.mp3')
            print("Local da música: ", caminhoMusica)
        
            url = QUrl.fromLocalFile(caminhoMusica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando musica...")

            else:
                print("Caminho ou arquivo não identificado... ")

        if musicaDele == "musica2" or musicaDele == "Musica2":
            caminhoMusica = os.path.join(os.path.dirname(__file__), 'audios', 'musica2.mp3')
            print("Local da música: ", caminhoMusica)

            url = QUrl.fromLocalFile(caminhoMusica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando musica...")

            else:
                print("Caminho ou arquivo não identificado... ")            

        if musicaDele == "musica3" or musicaDele == "Musica3":
            caminhoMusica = os.path.join(os.path.dirname(__file__), 'audios', 'musica3.mp3')
            print("Local da música: ", caminhoMusica)
        
            url = QUrl.fromLocalFile(caminhoMusica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando musica...")

            else:
                print("Caminho ou arquivo não identificado... ")

        if musicaDele == "musica4" or musicaDele == "Musica4":
            caminhoMusica = os.path.join(os.path.dirname(__file__), 'audios', 'musica4.mp3')
            print("Local da música: ", caminhoMusica)

            url = QUrl.fromLocalFile(caminhoMusica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando musica...")

            else:
                print("Caminho ou arquivo não identificado... ")

        if musicaDele == "musica5" or musicaDele == "Musica5":
            caminhoMusica = os.path.join(os.path.dirname(__file__), 'audios', 'musica5.mp3')
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
