# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex01.ui'
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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 20, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelCPF = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelCPF.setFont(font)
        self.labelCPF.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCPF.setObjectName("labelCPF")
        self.verticalLayout.addWidget(self.labelCPF)
        self.inputCPF = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inputCPF.setObjectName("inputCPF")
        self.verticalLayout.addWidget(self.inputCPF)
        self.buttonCPF = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonCPF.setObjectName("buttonCPF")
        self.verticalLayout.addWidget(self.buttonCPF)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 210, 301, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.inputMatematica = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.inputMatematica.setObjectName("inputMatematica")
        self.horizontalLayout.addWidget(self.inputMatematica)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(220, 260, 301, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.inputPortugues = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.inputPortugues.setObjectName("inputPortugues")
        self.horizontalLayout_2.addWidget(self.inputPortugues)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(220, 310, 301, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.inputConhecGerais = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.inputConhecGerais.setObjectName("inputConhecGerais")
        self.horizontalLayout_3.addWidget(self.inputConhecGerais)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(220, 360, 301, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.inputConhecEspec = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.inputConhecEspec.setObjectName("inputConhecEspec")
        self.horizontalLayout_4.addWidget(self.inputConhecEspec)
        self.labelDigiteNotas = QtWidgets.QLabel(self.centralwidget)
        self.labelDigiteNotas.setGeometry(QtCore.QRect(300, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelDigiteNotas.setFont(font)
        self.labelDigiteNotas.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDigiteNotas.setObjectName("labelDigiteNotas")
        self.labelNotaFInal = QtWidgets.QLabel(self.centralwidget)
        self.labelNotaFInal.setGeometry(QtCore.QRect(230, 460, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelNotaFInal.setFont(font)
        self.labelNotaFInal.setText("")
        self.labelNotaFInal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNotaFInal.setObjectName("labelNotaFInal")
        self.buttonConfirmarNotas = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConfirmarNotas.setGeometry(QtCore.QRect(380, 420, 111, 23))
        self.buttonConfirmarNotas.setObjectName("buttonConfirmarNotas")
        self.buttonCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCancelar.setGeometry(QtCore.QRect(270, 420, 75, 23))
        self.buttonCancelar.setObjectName("buttonCancelar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArquivo = QtWidgets.QMenu(self.menuBar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menuBar)
        self.actionCarregar = QtWidgets.QAction(MainWindow)
        self.actionCarregar.setObjectName("actionCarregar")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.menuArquivo.addAction(self.actionCarregar)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionSair)
        self.menuBar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelCPF.setText(_translate("MainWindow", "Digite seu CPF"))
        self.buttonCPF.setText(_translate("MainWindow", "Confirmar"))
        self.label_2.setText(_translate("MainWindow", "Matemática"))
        self.label_3.setText(_translate("MainWindow", "Português"))
        self.label_4.setText(_translate("MainWindow", "Conhec. Gerais"))
        self.label_5.setText(_translate("MainWindow", "Conhec. Espec."))
        self.labelDigiteNotas.setText(_translate("MainWindow", "Digite as suas notas "))
        self.buttonConfirmarNotas.setText(_translate("MainWindow", "Confirmar Notas"))
        self.buttonCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionCarregar.setText(_translate("MainWindow", "Carregar"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
