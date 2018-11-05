# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FEP(object):
    def setupUi(self, FEP):
        FEP.setObjectName("FEP")
        FEP.setEnabled(True)
        FEP.resize(1093, 248)
        FEP.setMinimumSize(QtCore.QSize(1093, 248))
        FEP.setMaximumSize(QtCore.QSize(1093, 248))
        FEP.setBaseSize(QtCore.QSize(1093, 248))
        FEP.setMouseTracking(True)
        FEP.setTabletTracking(True)
        FEP.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(FEP)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 0, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(7, 180, 1091, 23))
        self.progressBar.setProperty("value", 6)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 80, 151, 61))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        FEP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FEP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 21))
        self.menubar.setObjectName("menubar")
        self.menudenbingon = QtWidgets.QMenu(self.menubar)
        self.menudenbingon.setObjectName("menudenbingon")
        FEP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FEP)
        self.statusbar.setObjectName("statusbar")
        FEP.setStatusBar(self.statusbar)
        self.actionGITHUB = QtWidgets.QAction(FEP)
        self.actionGITHUB.setObjectName("actionGITHUB")
        self.menudenbingon.addSeparator()
        self.menudenbingon.addAction(self.actionGITHUB)
        self.menubar.addAction(self.menudenbingon.menuAction())

        self.retranslateUi(FEP)
        QtCore.QMetaObject.connectSlotsByName(FEP)

    def retranslateUi(self, FEP):
        _translate = QtCore.QCoreApplication.translate
        FEP.setWindowTitle(_translate("FEP", "FEP"))
        self.label.setText(_translate("FEP", "FEP - Fast Email Post - Быстрая Рассылка Электронных Писем"))
        self.pushButton.setText(_translate("FEP", "Начать"))
        self.menudenbingon.setTitle(_translate("FEP", "denbingon"))
        self.actionGITHUB.setText(_translate("FEP", "GITHUB"))
