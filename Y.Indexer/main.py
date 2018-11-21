import sys
import requests
from gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from random import choice
Response = 10
score = 0
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_YIndexer()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.AddData)
    def AddData(self):
        Requests = (self.ui.textEdit.toPlainText()).split('\n')
        Proxy = (self.ui.textEdit_2.toPlainText()).split('\n')
        BlackList = (self.ui.textEdit_3.toPlainText()).split('\n')
        OutputFileName = self.ui.lineEdit_2.text()
        TimeProxy = self.ui.horizontalSlider.value()
        UA = open('data/useragents.txt').read().split("\n")
        PR = open('data/proxies.txt').read().split('\n')
        for request in Requests:
            proxy = {'http': 'http://' + choice(PR)}
            useragnet = {'User-Agent': choice(UA)}
            konstr = f'https://yandex.ru/search/?text={request}'
            print(konstr)
            URL = requests.get(konstr, proxies=dict(http='socks5://9122027772:C9q8NfK@89.191.233.214:65233', https='socks5://9122027772:C9q8NfK@89.191.233.214:65233')).text
            print(URL)
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
