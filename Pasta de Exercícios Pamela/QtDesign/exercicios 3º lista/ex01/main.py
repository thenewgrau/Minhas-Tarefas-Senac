import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtWidgets, QtCore
from ex01 import Ui_MainWindow 

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        self.ui.buttonConfirmarNotas.clicked.connect(self.calcularNotas)
        self.ui.buttonCancelar.clicked.connect(self.limpezaGeral)
        self.ui.actionCarregar.triggered.connect(self.carregarProgram)
        self.ui.actionSalvar.triggered.connect(self.salvarProgram)
        self.ui.actionSair.triggered.connect(self.sairProgram)

    def calcularNotas(self):
        try:
            mat = float(self.ui.inputMatematica.text())
            port = float(self.ui.inputPortugues.text())
            conhecgerais = float(self.ui.inputConhecGerais.text())
            conhecespec = float(self.ui.inputConhecEspec.text())

            mat = (mat * 2) * 0.2
            port = (port * 2) * 0.2
            conhecespec = (conhecespec * 2) * 0.5
            conhecgerais = (conhecgerais * 2) * 0.1

            calcFinal = (mat + port + conhecespec + conhecgerais) / 4

            self.ui.labelNotaFInal.setText(f"Nota Final: {calcFinal:.2f}")

        except ValueError:
            self.ui.labelNotaFInal.setText("Erro! Coloque apenas números inteiros")


    def sairProgram(self):
        exit()
        
    def salvarProgram(self):
        data = {

            "CPF": self.ui.inputCPF.text(),
            "Matematica": self.ui.inputMatematica.text(),
            "Portugues": self.ui.inputPortugues.text(), 
            "Conhecimento Gerais": self.ui.inputConhecGerais.text(),
            "Conhecimento Especifico": self.ui.inputConhecEspec.text(),
        }

        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar Notas", "", "Arquivo JSON (*.json);;Todos os Arquivos (*.*)")

        if file_path:
            try:
                if not file_path.endswith('.json'):
                    file_path += '.json'
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                
                QtWidgets.QMessageBox.information(self, "Sucesso", "Notas Salvas com sucesso")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao salvar as notas: {e}")
        
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado!")

    
    def carregarProgram(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Carregar Notas", "", "Arquivos JSON (*.json);;Todos os Arquivos (*.*)")

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                self.ui.inputCPF.setText("")
                self.ui.inputMatematica.setText(data.get("Matematica", ""))
                self.ui.inputPortugues.setText(data.get("Portugues", ""))
                self.ui.inputConhecGerais.setText(data.get("Conhecimento Gerais", ""))
                self.ui.inputConhecEspec.setText(data.get("Conhecimento Especifico", ""))

                QtWidgets.QMessageBox.information(self, "Sucesso", "Notas Carregadas com sucesso")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar as notas: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado!")

    def limpezaGeral(self):
        self.ui.inputCPF.setText("")
        self.ui.inputMatematica.setText("")
        self.ui.inputPortugues.setText("")
        self.ui.inputConhecGerais.setText("")
        self.ui.inputConhecEspec.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())
