import smtplib
import email
import mimetypes
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.header import Header
from base64 import encodebytes
from gui import *
from PyQt5 import *
from datetime import datetime
mail_coding = 'windows-1251'
class BaseWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SmallMailer()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MailPost)
        self.ui.pushButton_2.clicked.connect(self.save_smtp)
        self.ui.progressBar.setValue(0)
        self.ui.textBrowser_2.append('Program is start ' + datetime.strftime(datetime.now(), "%H:%M:%S")) #логи
        try:
            sav = open("data/account.txt", 'r')
            save = sav.read()
            data = save.split("\n")
            self.ui.lineEdit_3.setText(data[0][::-1])
            self.ui.lineEdit_5.setText(data[1][::-1])
            self.ui.lineEdit_4.setText(data[2][::-1])
            self.ui.lineEdit_6.setText(data[3][::-1])
        except:
            self.ui.textBrowser_2.append('Program isn\'t found a save file ' + datetime.strftime(datetime.now(), "%H:%M:%S")) #логи
    def save_smtp(self):
        smtp = self.ui.lineEdit_3.text()[::-1]
        smtp_p = self.ui.lineEdit_5.text()[::-1]
        user = self.ui.lineEdit_4.text()[::-1]
        passw = self.ui.lineEdit_6.text()[::-1]
        try:
            os.mkdir("data")
        except:
            self.ui.textBrowser_2.append('Catalog is already have ' + datetime.strftime(datetime.now(), "%H:%M:%S")) #логи
        save = open("data/account.txt", 'w')
        save.write(f'{smtp}\n{smtp_p}\n{user}\n{passw}')
        save.close()
        self.ui.textBrowser_2.append('Susseful save ' + datetime.strftime(datetime.now(), "%H:%M:%S"))
    def MailPost(self):
        self.ui.textBrowser_2.append('Search a text ' + datetime.strftime(datetime.now(), "%H:%M:%S")) #логи
        #Некие переменные
        kolvo = 0
        scro = 1
        #Достаем информацию из полей
        smtp = self.ui.lineEdit_3.text()
        smtp_p = self.ui.lineEdit_5.text()
        user = self.ui.lineEdit_4.text()
        passw = self.ui.lineEdit_6.text()
        base_mail = self.ui.textEdit.toPlainText()
        mail_post = self.ui.lineEdit.text()
        title = self.ui.lineEdit_2.text()
        text = self.ui.textEdit_3.toPlainText()
        signa = self.ui.textEdit_2.toPlainText()
        #Конфигурация текста письма
        text_mail = f"""{text}
{'_' * 40}
{signa}"""
        #Конфигурация письма перед отправкой
        multi_letter = MIMEMultipart()
        multi_letter['To'] = base_mail
        multi_letter['From'] = mail_post
        multi_letter['Subject'] =  title
        letter = MIMEText(text_mail.encode('cp1251'), 'plain', mail_coding)
        letter.set_charset(mail_coding)
        multi_letter.attach(letter)
        #Адреса в удобный вид для использования
        kolv = base_mail.split('\n')
        self.ui.textBrowser_2.append('Считаю кол-во адресатов ' + datetime.strftime(datetime.now(), "%H:%M:%S")) #Логи
        #Кол-во адресатов
        for kol in kolv:
            kolvo += 1
        self.ui.textBrowser_2.append('Запускаю функцию отправки ' + datetime.strftime(datetime.now(), "%H:%M:%S")) #Логи
        #Старт smtp библиотеки
        postMail = smtplib.SMTP(smtp, smtp_p)
        postMail.starttls()
        postMail.login(user, passw)
        #Отправка сообщений
        for mail in kolv:
            #Отправка
            del multi_letter['To']
            multi_letter['To'] = mail
            postMail.sendmail(mail_post, mail, multi_letter.as_string())
            #Прогресс бар
            progress = int(scro/kolvo*100)
            self.ui.progressBar.setValue(progress)
            scro += 1
        #Закрываем соединение
        postMail.quit()
        self.ui.textBrowser_2.append('Успешно ' + datetime.strftime(datetime.now(), "%H:%M:%S" + '\n')) #Логи
        self.ui.progressBar.setValue(0)
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = BaseWindow()
    myapp.show()
    sys.exit(app.exec_())
