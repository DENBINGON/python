# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YIndexerGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YIndexer(object):
    def setupUi(self, YIndexer):
        YIndexer.setObjectName("YIndexer")
        YIndexer.setEnabled(True)
        YIndexer.resize(831, 503)
        YIndexer.setMinimumSize(QtCore.QSize(831, 503))
        YIndexer.setMaximumSize(QtCore.QSize(831, 503))
        YIndexer.setSizeIncrement(QtCore.QSize(831, 503))
        YIndexer.setBaseSize(QtCore.QSize(831, 503))
        YIndexer.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(YIndexer)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 50, 871, 16))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(680, 90, 151, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 450, 191, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 90, 291, 391))
        self.textEdit.setLineWidth(0)
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 70, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 90, 141, 191))
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_2.setMaximumSize(QtCore.QSize(141, 391))
        self.textEdit_2.setSizeIncrement(QtCore.QSize(141, 391))
        self.textEdit_2.setBaseSize(QtCore.QSize(141, 391))
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(450, 120, 221, 22))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider.setMaximum(60)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 90, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 140, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(650, 140, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(450, 160, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(450, 180, 221, 181))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 450, 191, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(450, 370, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 390, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(450, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(450, 410, 221, 41))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(300, 300, 141, 181))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 280, 101, 21))
        self.label_10.setObjectName("label_10")
        YIndexer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YIndexer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName("menubar")
        self.menuDBG = QtWidgets.QMenu(self.menubar)
        self.menuDBG.setObjectName("menuDBG")
        self.menuSYSTEM = QtWidgets.QMenu(self.menubar)
        self.menuSYSTEM.setObjectName("menuSYSTEM")
        YIndexer.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuDBG.menuAction())
        self.menubar.addAction(self.menuSYSTEM.menuAction())

        self.retranslateUi(YIndexer)
        QtCore.QMetaObject.connectSlotsByName(YIndexer)

    def retranslateUi(self, YIndexer):
        _translate = QtCore.QCoreApplication.translate
        YIndexer.setWindowTitle(_translate("YIndexer", "MainWindow"))
        self.label.setText(_translate("YIndexer", "Y.Indexer"))
        self.label_2.setText(_translate("YIndexer", "by DEnBInGOn"))
        self.label_3.setText(_translate("YIndexer", "Логи:"))
        self.pushButton.setText(_translate("YIndexer", "Начать"))
        self.label_4.setText(_translate("YIndexer", "Поисковые запросы: "))
        self.label_5.setText(_translate("YIndexer", "Прокси:"))
        self.label_6.setText(_translate("YIndexer", "Время на один прокси:"))
        self.label_7.setText(_translate("YIndexer", "0"))
        self.label_8.setText(_translate("YIndexer", "60"))
        self.label_9.setText(_translate("YIndexer", "Черный лист:"))
        self.pushButton_2.setText(_translate("YIndexer", "Сохранить настройки"))
        self.label_11.setText(_translate("YIndexer", "Имя сохраняемого файла:"))
        self.label_12.setText(_translate("YIndexer", "Настройки:"))
        self.checkBox.setText(_translate("YIndexer", "Использовать User-Agent (Recommend)"))
        self.label_10.setText(_translate("YIndexer", "Баненые прокси:"))
        self.menuDBG.setTitle(_translate("YIndexer", "DBG"))
        self.menuSYSTEM.setTitle(_translate("YIndexer", "SYSTEM"))

