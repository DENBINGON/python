# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fepgui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SmallMailer(object):
    def setupUi(self, SmallMailer):
        SmallMailer.setObjectName("SmallMailer")
        SmallMailer.resize(800, 650)
        SmallMailer.setMinimumSize(QtCore.QSize(800, 650))
        SmallMailer.setMaximumSize(QtCore.QSize(800, 650))
        SmallMailer.setSizeIncrement(QtCore.QSize(800, 650))
        SmallMailer.setBaseSize(QtCore.QSize(800, 650))
        self.centralwidget = QtWidgets.QWidget(SmallMailer)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -10, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setIndent(-1)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 0, 821, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 311, 481))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 70, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 50, 191, 21))
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(330, 530, 501, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 510, 121, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 130, 221, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 90, 121, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 110, 311, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 460, 81, 21))
        self.label_9.setObjectName("label_9")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 480, 311, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 480, 144, 33))
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(650, 50, 111, 21))
        self.label_10.setObjectName("label_10")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(650, 70, 141, 391))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(330, 150, 311, 311))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 550, 91, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 570, 81, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(410, 570, 81, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 593, 61, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(410, 595, 71, 31))
        self.label_15.setObjectName("label_15")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 570, 311, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 600, 311, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(480, 570, 71, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(480, 600, 311, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(640, 570, 70, 21))
        self.checkBox.setObjectName("checkBox")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(560, 570, 81, 21))
        self.label_16.setObjectName("label_16")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(686, 555, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        SmallMailer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SmallMailer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menudenbingon = QtWidgets.QMenu(self.menubar)
        self.menudenbingon.setObjectName("menudenbingon")
        self.menuGitHub = QtWidgets.QMenu(self.menudenbingon)
        self.menuGitHub.setObjectName("menuGitHub")
        self.menuVK = QtWidgets.QMenu(self.menudenbingon)
        self.menuVK.setObjectName("menuVK")
        SmallMailer.setMenuBar(self.menubar)
        self.actionLINK = QtWidgets.QAction(SmallMailer)
        self.actionLINK.setObjectName("actionLINK")
        self.actionLINK_2 = QtWidgets.QAction(SmallMailer)
        self.actionLINK_2.setObjectName("actionLINK_2")
        self.menuGitHub.addAction(self.actionLINK)
        self.menuVK.addAction(self.actionLINK_2)
        self.menudenbingon.addAction(self.menuGitHub.menuAction())
        self.menudenbingon.addAction(self.menuVK.menuAction())
        self.menubar.addAction(self.menudenbingon.menuAction())

        self.retranslateUi(SmallMailer)
        QtCore.QMetaObject.connectSlotsByName(SmallMailer)

    def retranslateUi(self, SmallMailer):
        _translate = QtCore.QCoreApplication.translate
        SmallMailer.setWindowTitle(_translate("SmallMailer", "SmallMailer"))
        self.label.setText(_translate("SmallMailer", "Small Mailer"))
        self.label_2.setText(_translate("SmallMailer", "by DENBINGON"))
        self.label_3.setText(_translate("SmallMailer", "Enter email base: "))
        self.label_4.setText(_translate("SmallMailer", "________________________________________________________________________________________________________________________________________________"))
        self.label_5.setText(_translate("SmallMailer", "Mail from post:"))
        self.label_6.setText(_translate("SmallMailer", "Progress:"))
        self.label_7.setText(_translate("SmallMailer", "Enter text or html to post:"))
        self.label_8.setText(_translate("SmallMailer", "Title:"))
        self.label_9.setText(_translate("SmallMailer", "Sigature:"))
        self.pushButton.setText(_translate("SmallMailer", "Начать"))
        self.label_10.setText(_translate("SmallMailer", "Logs:"))
        self.label_11.setText(_translate("SmallMailer", "Auth:"))
        self.label_12.setText(_translate("SmallMailer", "SMTP Server:"))
        self.label_13.setText(_translate("SmallMailer", "SMTP Port:"))
        self.label_14.setText(_translate("SmallMailer", "Login:"))
        self.label_15.setText(_translate("SmallMailer", "Password:"))
        self.checkBox.setText(_translate("SmallMailer", "Yes"))
        self.label_16.setText(_translate("SmallMailer", "Want SSL/TLS?"))
        self.pushButton_2.setText(_translate("SmallMailer", "Save SMTP"))
        self.menudenbingon.setTitle(_translate("SmallMailer", "denbingon"))
        self.menuGitHub.setTitle(_translate("SmallMailer", "GitHub"))
        self.menuVK.setTitle(_translate("SmallMailer", "VK"))
        self.actionLINK.setText(_translate("SmallMailer", "LINK"))
        self.actionLINK_2.setText(_translate("SmallMailer", "LINK"))