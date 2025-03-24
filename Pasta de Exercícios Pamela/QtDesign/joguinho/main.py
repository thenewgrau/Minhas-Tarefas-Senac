import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtWidgets, QtCore
from jogoLegal import Ui_MainWindow

class jogoDivertido(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        self.ui.carregarJogo.clicked.connect(self.carregarJogo)
        self.ui.salvarJogo.clicked.connect(self.salvarJogo)
        self.ui.novoJogo.clicked.connect(self.novoJogo)
        self.ui.sairJogo.clicked.connect(self.sairJogo)

    def novoJogo(self):
        self.ui.lineEditNome.clear()
        self.ui.lineEditIdade.clear()
        self.ui.lineEditAltura.clear()
        self.ui.dateEdit.clear()
        self.ui.radioButtonFeminino.setChecked(False)
        self.ui.radioButtonMasculino.setChecked(False)

    def salvarJogo(self):
        data = {
            "nome": self.ui.lineEditNome.text(),
            "dataNascimento": self.ui.dateEdit.date().toString("yyyy/MM/dd"),
            "idade": self.ui.lineEditIdade.text(),
            "altura": self.ui.lineEditAltura.text(),
            "sexo": "Feminino" if self.ui.radioButtonFeminino.isChecked()
            else "Masculino" if self.ui.radioButtonMasculino.isChecked() else "Não informado."
        }

        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar Jogo", "", "Arquivo JSON (*.json);;Todos os Arquivos (*.*)")

        if file_path:
            try:
                if not file_path.endswith('.json'):
                    file_path += '.json'
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                
                QtWidgets.QMessageBox.information(self, "Sucesso", "Jogo Salvo com sucesso")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao salvar o jogo: {e}")
        
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado!")

    def carregarJogo(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Carregar Jogo", "", "Arquivos JSON (*.json);;Todos os Arquivos (*.*)")

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                self.ui.lineEditNome.setText(data.get("nome", ""))
                self.ui.dateEdit.setDate(QtCore.QDate.fromString(data.get("dataNascimento", ""), "yyyy/MM/dd"))
                self.ui.lineEditIdade.setText(data.get("idade", ""))
                self.ui.lineEditAltura.setText(data.get("altura", ""))
                
                if data.get("sexo") == "Feminino":
                    self.ui.radioButtonFeminino.setChecked(True)
                elif data.get("sexo") == "Masculino":
                    self.ui.radioButtonMasculino.setChecked(True)
                else:
                    self.ui.radioButtonFeminino.setChecked(False)
                    self.ui.radioButtonMasculino.setChecked(False)

                QtWidgets.QMessageBox.information(self, "Sucesso", "Jogo Carregado com sucesso")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar o jogo: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado!")

    def sairJogo(self):
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = jogoDivertido()
    window.show()
    sys.exit(app.exec_())
