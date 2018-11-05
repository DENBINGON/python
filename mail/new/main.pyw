import smtplib
import sys
from gui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FEP()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MyFunction)
    def MyFunction(self):
        progress = 0
        Dat = []
        MailList = []
        SET = open("data/set.txt")
        for line in range(14):
            Dat.append(SET.readline())
        del line
        MailVal = 2
        SET.close()
        def POST(mail_otp, mail_kom, text, progr):
            smtpObj = smtplib.SMTP(Dat[2],Dat[4])
            smtpObj.starttls()
            smtpObj.login(Dat[8],Dat[10])
            smtpObj.sendmail(mail_otp, mail_kom, text)
            smtpObj.quit()
            print(str(progr/MailVal*100) + "%")

        mail = open("data/database_mail.txt")
        for line in range(MailVal):
            MailList.append(mail.readline())
        mail.close()
        Dat = [line.rstrip() for line in Dat]
        MailList = [line.rstrip() for line in MailList]
        print("Start")
        textI = input("Print some text to post")
        try:
            for MailAd in MailList:
                progress += 1
                POST(Dat[8], MailAd, textI, progress)
            print('The END')
        except:
            print("Script has error")

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
