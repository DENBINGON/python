import sys
from gui import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QTableWidgetItem
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.valueRowInSklad = 0
        self.valueRowInOrdered = 0
        self.ui.pushButton_addRow.clicked.connect(self.Row)
        self.ui.pushButton_2.clicked.connect(self.DRow)
        self.ui.pushButton_retry.clicked.connect(self.Retry)
        self.ui.pushButton_3.clicked.connect(self.Ordered)
        self.ui.pushButton_4.clicked.connect(self.Susseful)
    def Susseful(self):
        dataSusseful = []
        def Retry(self):
            DATA = []
            goToReserv = []
            EndX = 0
            valueRowInEnds = 0
            IDfor = 0
            self.ui.tableWidget_ends.clearContents()
            self.ui.tableWidget_ends.setRowCount(0)
            for row in range(int(self.ui.tableWidget_sklad.rowCount())):
                item = QTableWidgetItem()
                item.setText(str(IDfor))
                self.ui.tableWidget_sklad.setItem(IDfor, 2, item)
                IDfor += 1
            for row in range(int(self.ui.tableWidget_sklad.rowCount())):
                try:
                    Name = self.ui.tableWidget_sklad.item(row, 0).text()
                except:
                    Name = ''
                try:
                    Vallue = self.ui.tableWidget_sklad.item(row, 1).text()
                except:
                    Vallue = ''
                try:
                    ID = self.ui.tableWidget_sklad.item(row, 2).text()
                except:
                    ID = ''
                DATA.append({
                'NAME': Name,
                'VALLUE': Vallue,
                'ID': ID
                })
            for checkCost in DATA:
                try:
                    if int(checkCost['VALLUE']) == 0:
                        goToReserv.append(checkCost)
                except:
                    print('No provide a item')
            for access in goToReserv:
                print(access)
                valueRowInEnds += 1
                self.ui.tableWidget_ends.setRowCount(valueRowInEnds)
                item = QTableWidgetItem()
                item.setText(access['ID'])
                self.ui.tableWidget_ends.setItem(EndX, 0, item)
                item = QTableWidgetItem()
                item.setText(access['NAME'])
                self.ui.tableWidget_ends.setItem(EndX, 1, item)
                item = QTableWidgetItem()
                item.setText(access['VALLUE'])
                self.ui.tableWidget_ends.setItem(EndX, 2, item)
                EndX += 1
        #-----------------------------------------------------------------------
        try:
            Number = int(self.ui.lineEdit_2.text()) - 1
            self.ui.lineEdit_2.clear()
        except:
            pass
        try:
            ID = int(self.ui.tableWidget_ordered.item(Number, 0).text())
            Vallue = self.ui.tableWidget_ordered.item(Number, 2).text()
            if Vallue != 0:
                item = QTableWidgetItem()
                val = str(Vallue)
                item.setText(val)
                self.ui.tableWidget_sklad.setItem(ID, 1, item)
            RETRY = Retry(self)
        except:
            pass
        for row in range(self.ui.tableWidget_ordered.rowCount()):
            if row != Number:
                dataSusseful.append({
                'ID': self.ui.tableWidget_ordered.item(row, 0).text(),
                'NAME': self.ui.tableWidget_ordered.item(row, 1).text(),
                'VALLUE': self.ui.tableWidget_ordered.item(row, 2).text()
                })
        self.ui.tableWidget_ordered.clearContents()
        self.ui.tableWidget_ordered.setRowCount(0)
        self.valueRowInOrdered = 0
        for data in dataSusseful:
            self.valueRowInOrdered += 1
            num = int(self.valueRowInOrdered)
            self.ui.tableWidget_ordered.setRowCount(num)

            item = QTableWidgetItem()
            item.setText(data['ID'])
            self.ui.tableWidget_ordered.setItem(num-1, 0, item)

            item = QTableWidgetItem()
            item.setText(data['NAME'])
            self.ui.tableWidget_ordered.setItem(num-1, 1, item)

            item = QTableWidgetItem()
            item.setText(data['VALLUE'])
            self.ui.tableWidget_ordered.setItem(num-1, 2, item)
            print(data)
    def Ordered(self):
        num = int(self.valueRowInOrdered)
        try:
            Number = int(self.ui.lineEdit.text()) - 1
            self.ui.lineEdit.clear()
        except:
            pass
        checkID = []
        try:
            for row in range(int(self.ui.tableWidget_ordered.rowCount())):
                try:
                    checkID.append(self.ui.tableWidget_ordered.item(row, 0).text())
                except:
                    pass
        except:
            pass
        try:
            if self.ui.tableWidget_ends.item(Number, 0).text() not in checkID:
                try:
                    self.valueRowInOrdered += 1
                    Name = self.ui.tableWidget_ends.item(Number, 1).text()
                    Vallue = self.ui.tableWidget_ends.item(Number, 2).text()
                    ID = self.ui.tableWidget_ends.item(Number, 0).text()
                    self.ui.tableWidget_ordered.setRowCount(num)
                    item = QTableWidgetItem()
                    item.setText(Name)
                    self.ui.tableWidget_ordered.setItem(num-1, 1, item)
                    item = QTableWidgetItem()
                    item.setText(Vallue)
                    self.ui.tableWidget_ordered.setItem(num-1, 2, item)
                    item = QTableWidgetItem()
                    item.setText(ID)
                    self.ui.tableWidget_ordered.setItem(num-1, 0, item)
                except:
                    pass
        except:
            pass
    def Retry(self):
        DATA = []
        goToReserv = []
        EndX = 0
        valueRowInEnds = 0
        IDfor = 0
        self.ui.tableWidget_ends.clearContents()

        for row in range(int(self.ui.tableWidget_sklad.rowCount())):
            item = QTableWidgetItem()
            item.setText(str(IDfor))
            self.ui.tableWidget_sklad.setItem(IDfor, 2, item)
            IDfor += 1
        for row in range(int(self.ui.tableWidget_sklad.rowCount())):
            try:
                Name = self.ui.tableWidget_sklad.item(row, 0).text()
            except:
                Name = ''
            try:
                Vallue = self.ui.tableWidget_sklad.item(row, 1).text()
            except:
                Vallue = ''
            try:
                ID = self.ui.tableWidget_sklad.item(row, 2).text()
            except:
                ID = ''
            DATA.append({
            'NAME': Name,
            'VALLUE': Vallue,
            'ID': ID
            })
        for checkCost in DATA:
            try:
                if int(checkCost['VALLUE']) == 0:
                    goToReserv.append(checkCost)
            except:
                print('No provide a item')
        for access in goToReserv:
            print(access)
            valueRowInEnds += 1
            self.ui.tableWidget_ends.setRowCount(valueRowInEnds)
            item = QTableWidgetItem()
            item.setText(access['ID'])
            self.ui.tableWidget_ends.setItem(EndX, 0, item)
            item = QTableWidgetItem()
            item.setText(access['NAME'])
            self.ui.tableWidget_ends.setItem(EndX, 1, item)
            item = QTableWidgetItem()
            item.setText(access['VALLUE'])
            self.ui.tableWidget_ends.setItem(EndX, 2, item)
            EndX += 1
    def Row(self):
        self.valueRowInSklad += 1
        self.ui.tableWidget_sklad.setRowCount(self.valueRowInSklad)
    def DRow(self):
        self.valueRowInSklad -= 1
        self.ui.tableWidget_sklad.setRowCount(self.valueRowInSklad)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
