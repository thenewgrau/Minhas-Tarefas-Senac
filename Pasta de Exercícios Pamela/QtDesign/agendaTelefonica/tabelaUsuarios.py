# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabelaUsuarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabelaUsuarios = QtWidgets.QTableWidget(self.centralwidget)
        self.tabelaUsuarios.setGeometry(QtCore.QRect(200, 100, 441, 341))
        self.tabelaUsuarios.setObjectName("tabelaUsuarios")
        self.tabelaUsuarios.setColumnCount(0)
        self.tabelaUsuarios.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.botaoRemover = QtWidgets.QPushButton(self.centralwidget)
        self.botaoRemover.setGeometry(QtCore.QRect(310, 460, 75, 23))
        self.botaoRemover.setObjectName("botaoRemover")
        self.botaoEditar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEditar.setGeometry(QtCore.QRect(450, 460, 75, 23))
        self.botaoEditar.setObjectName("botaoEditar")
        self.botaoVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVoltar.setGeometry(QtCore.QRect(710, 20, 75, 23))
        self.botaoVoltar.setObjectName("botaoVoltar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Usuários Cadastrados"))
        self.botaoRemover.setText(_translate("MainWindow", "Remover"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoVoltar.setText(_translate("MainWindow", "voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
