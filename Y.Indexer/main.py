import sys
import requests
from gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from random import choice
import xlsxwriter
from datetime import datetime
import time     #isTristate
import os
class YINDEXER(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_YIndexer()
        self.ui.setupUi(self)
        try:
            dataSaveBlackList = open('data/Settings/BlackList.txt', 'r').read().split('\n')
            dataSaveProxy = open('data/Settings/Proxy.txt', 'r').read().split('\n')
            dataSaveOutAndTime = open('data/Settings/OutAndTime.txt', 'r').read().split('\n')
            for dataS in dataSaveProxy:
                self.ui.textEdit_2.append(dataS)
            for dataSa in dataSaveBlackList:
                self.ui.textEdit_3.append(dataSa)
            self.ui.lineEdit_2.setText(dataSaveOutAndTime[0])
            self.ui.horizontalSlider.setValue(int(dataSaveOutAndTime[1]))
            self.ui.textBrowser.append('Сохаранение найдено ')
        except:
            self.ui.textBrowser.append('Сохаранение не найдено ')
        self.ui.textBrowser.append('Старт программы ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        self.ui.pushButton.clicked.connect(self.AddData)
        self.ui.pushButton_2.clicked.connect(self.SaveSettings)
    def SaveSettings(self):
        Proxy = (self.ui.textEdit_2.toPlainText()).split('\n')
        BlackList = (self.ui.textEdit_3.toPlainText()).split('\n')
        OutputFileName = self.ui.lineEdit_2.text()
        TimeProxy = self.ui.horizontalSlider.value()
        try:
            os.mkdir("data/Settings")
        except:
            self.ui.textBrowser.append('Перезапись ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        p = open('data/Settings/Proxy.txt', 'w')
        for Prox in Proxy:
            p.write(Prox + '\n')
        p.close()
        b = open('data/Settings/BlackList.txt', 'w')
        for BlackLis in BlackList:
            b.write(BlackLis + '\n')
        b.close()
        ot = open('data/Settings/OutAndTime.txt', 'w')
        ot.write(OutputFileName + '\n' + str(TimeProxy))
        ot.close()
        self.ui.textBrowser.append('Успешно сохраненно ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
    def AddData(self):
        pl = 0
        self.ui.textBrowser.append('Старт ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        UsedProxy = []
        UsedRequest = []
        indexP = 0
        B=int(1)
        Ai=int(1)
        ProxyData = []
        stat = 0
        progress = 0
        val = 0
        cola = 0
        self.ui.progressBar.setValue(0)
        Requests = (self.ui.textEdit.toPlainText()).split('\n')
        Proxy = (self.ui.textEdit_2.toPlainText()).split('\n')
        BlackList = (self.ui.textEdit_3.toPlainText()).split('\n')
        OutputFileName = self.ui.lineEdit_2.text()
        TimeProxy = self.ui.horizontalSlider.value()
        av = open('data/useragents.txt').read().split("\n")
        for AV in av:
            pl += 1
        av.remove(av[pl-1])
        for i in Requests:
            val += 1
        for po in Proxy:
            cola += 1
        self.ui.textBrowser.append('Сбор данных окончен ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        saveWriter = xlsxwriter.Workbook(OutputFileName + '.xlsx')
        writer = saveWriter.add_worksheet()
        self.ui.textBrowser.append('Начало парсинга и записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        if indexP == cola:
            indexP = 0
        proxyToUrl = 'http://' + Proxy[indexP]
        for request in Requests:
            DATA = []
            stat += 1
            try:
                url = 'https://yandex.ru/search/?text=' + request
                headers = {
                'User-Agent': choice(av),
                'From': 'denbingon@denbingon.com'
                }
                if self.ui.checkBox.checkState() == 2:
                    responze = requests.get(url, proxies={'http': proxyToUrl},headers=headers).text
                else:
                    responze = requests.get(url, proxies={'http': proxyToUrl}).text
                YandexHTML = BeautifulSoup(responze, 'html.parser')
                try:
                    html = YandexHTML.find('div', class_='serp-list')
                    for div in html.find_all('div', class_='serp-item'):
                        DomainCheckBlack = []
                        try:
                            try:
                                A = div.find_all('a', class_='link serp-url__link')[0]['href']
                            except:
                                A = div.find_all('a', class_='link serp-url__link i-bem link_js_inited')[0]['href']
                        except:
                            A = 'Erorr'
                        if A != 'Erorr':
                            DomainCheckBlack = (A).split('/')
                            if DomainCheckBlack[2] in BlackList:
                                self.ui.textBrowser.append('Найден элемент черного листа ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                        DATA.append(A)
                except:
                    self.ui.textBrowser.append('Proxy baned ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    self.ui.textEdit_4.append(Proxy[indexP] + '\n')
                writer.write(f'A{Ai}', request)
                Ai += 1
                try:
                    try:
                        writer.write(f'B{B}', DATA[0])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'C{B}', DATA[1])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'D{B}', DATA[2])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'E{B}', DATA[3])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'F{B}', DATA[4])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'G{B}', DATA[5])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'H{B}', DATA[6])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'I{B}', DATA[7])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'J{B}', DATA[8])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    try:
                        writer.write(f'K{B}', DATA[9])
                    except:
                        self.ui.textBrowser.append('Не найден элемент для записи ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    B += 1
                except:
                    self.ui.textBrowser.append('Запись не удалась ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                aaa = stat/val*100
                time.sleep(TimeProxy)
                UsedRequest.append(request)
            except:
                if Proxy == []:
                    self.ui.textBrowser.append('Прокси кончились ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
                    break
                if indexP == cola:
                    indexP = 0
                UsedProxy.append(Proxy[indexP])
                indexP += 1
                proxyToUrl = 'http://' + Proxy[indexP]
                continue
            self.ui.progressBar.setValue(aaa)
        saveWriter.close()
        wr = open('data/UsedProxy.txt', 'w')
        for wor in UsedProxy:
            wr.write(wor + '\n')
        wr.close()
        ur = open('data/UsedRequests.txt', 'w')
        for reques in UsedRequest:
            ur.write(reques + '\n')
        ur.close()
        self.ui.textBrowser.append('Успешно ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = YINDEXER()
    myapp.show()
    sys.exit(app.exec_())                                                                                                                         
