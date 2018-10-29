import smtplib
IndexEM = 0
Dat = []
MailList = []
select = input(""" Выберите что вы хотите сделать
1.Засрать кому-нибудь почту
2.Массовая рассылка
""")
SET = open("data/settings.txt")
for line in range(14):
    Dat.append(SET.readline())
del line
MailVal = int(Dat[13])
SET.close()
mail = open("data/database_mail.txt")
for line in range(MailVal):
    MailList.append(mail.readline())
mail.close()
Dat = [line.rstrip() for line in Dat]
MailList = [line.rstrip() for line in MailList]
print("Start")

smtpObj = smtplib.SMTP(Dat[2],Dat[4])
smtpObj.starttls()
smtpObj.login(Dat[8],Dat[10])
if select == 2:
    for HaveMail in range(len(MailList)):
        smtpObj.sendmail(Dat[8],MailList[IndexEM],"Test TEXT READ AND SEND")
        IndexEM += 1
else:
    Adres = input("Кому: ")
    Val = int(input("Сколько: "))
    for val in range(Val):
        smtpObj.sendmail(Dat[8],Adres,"AHAHAAAAHAAHAAHAHAHAAH")
smtpObj.quit()

print('The END')
