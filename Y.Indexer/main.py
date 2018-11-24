import sys
import requests
from gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from random import choice
import xlsxwriter
from datetime import datetime
import time
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_YIndexer()
        self.ui.setupUi(self)
        self.ui.textBrowser.append('ВЫ ИСПОЛЬЗУЕТЕ ДЕМО ВЕРСИЮ ПРОГРАММЫ ')
        self.ui.textBrowser.append('Старт программы ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        self.ui.pushButton.clicked.connect(self.AddData)
    def AddData(self):
        self.ui.textBrowser.append('Старт ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        B=int(1)
        Ai=int(1)
        ProxyData = []
        stat = 0
        progress = 0
        val = 0
        self.ui.progressBar.setValue(0)
        Requests = (self.ui.textEdit.toPlainText()).split('\n')
        Proxy = (self.ui.textEdit_2.toPlainText()).split('\n')
        BlackList = (self.ui.textEdit_3.toPlainText()).split('\n')
        OutputFileName = self.ui.lineEdit_2.text()
        TimeProxy = self.ui.horizontalSlider.value()
        UA = open('data/useragents.txt').read().split("\n")
        for i in Requests:
            val += 1
        self.ui.textBrowser.append('Сбор данных окончен ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        saveWriter = xlsxwriter.Workbook(OutputFileName + '.xlsx')
        writer = saveWriter.add_worksheet()
        self.ui.textBrowser.append('Начало парсинга и записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        for request in Requests:
            goai = 0
            DATA = []
            stat+=1
            proxyToUrl = 'http://' + choice(Proxy)
            url = 'https://yandex.ru/search/?text=' + request
            headers = {
            'User-Agent': choice(UA),
            'From': 'denbingon@denbingon.com'
            }
            responze = requests.get(url, proxies={'http': proxyToUrl},headers=headers).text
            print(responze)
            YandexHTML = BeautifulSoup(responze, 'html.parser').find('div', class_='serp-list')
            try:
                for div in YandexHTML.find_all('div', class_='serp-item'):
                    try:
                        try:
                            A = div.find_all('a', class_='link serp-url__link')[0]['href']
                        except:
                            A = div.find_all('a', class_='link serp-url__link i-bem link_js_inited')[0]['href']
                    except:
                        A = 'Erorr'
                    print(A)
                    DATA.append(A)
                    goai += 1
            except:
                self.ui.textBrowser.append('Proxy baned ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
            writer.write(f'A{Ai}', request)
            Ai+=goai
            for data in DATA:
                writer.write(f'B{B}', data)
                B += 1
            aaa = stat/val*100
            print (aaa)
            self.ui.progressBar.setValue(aaa)
            del DATA
            del goai
            time.sleep(TimeProxy)
        saveWriter.close()
        self.ui.textBrowser.append('Успешно ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())                                                                                                                         
