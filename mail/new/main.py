import smtplib
import sys
from gui import *
from PyQt5 import *
from datetime import datetime
tls = 0
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SmallMailer()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MailPost)
        self.ui.progressBar.setValue(0)
        self.ui.textBrowser_2.append('Program is start ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        self.ui.checkBox.stateChanged.connect(self.TLS)
    def TLS(self):
        tls = 1
    def MailPost(self):
        self.ui.textBrowser_2.append('Search a text ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        kolvo = 0
        scro = 1
        smtp = self.ui.lineEdit_3.text()
        smtp_p = self.ui.lineEdit_5.text()
        user = self.ui.lineEdit_4.text()
        passw = self.ui.lineEdit_6.text()
        base_mail = self.ui.textEdit.toPlainText()
        mail_post = self.ui.lineEdit.text()
        title = self.ui.lineEdit_2.text()
        text = self.ui.textEdit_3.toPlainText()
        signa = self.ui.textEdit_2.toPlainText()
        kolv = base_mail.split('\n')
        self.ui.textBrowser_2.append('Считаю кол-во адресатов ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        for kol in kolv:
            kolvo += 1
        self.ui.textBrowser_2.append('Запускаю функцию отправки ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
        smtpObj = smtplib.SMTP(smtp, smtp_p)
        if tls == 1:
            smtpObj.starttls()
        smtpObj.login(user, passw)
        for mail in kolv:
            smtpObj.sendmail(mail_post, mail, text)
            progress = int(scro/kolvo*100)
            self.ui.progressBar.setValue(progress)
            scro += 1
        smtpObj.quit()
        self.ui.textBrowser_2.append('Успешно ' + datetime.strftime(datetime.now(), "%H:%M:%S" + '\n'))
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
