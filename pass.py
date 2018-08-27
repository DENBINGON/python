print ('Hello! Registration: ')
username = input('Please, enter username: ')
password_1 = input('Enter password: ')
password_2 = input('Reenter password: ')
email_1 = input('Enter mail: ')
email_2 = input('Reenter mail: ')
if password_1 == password_2 and email_1 == email_2:
    print ('Hello, ', username, ', Ваши данные спиженны и отправлены на сервер :\') ')
    f = open('output.txt', 'w', encoding='utf-8')
    f.write('name: ' , username , ' password: ' , password_1 , ' email: ' , email_1 )
else:
    print ('Password wrong')
stop = input('STOP')
