import requests
import xlsxwriter
from bs4 import BeautifulSoup
key = open('data/key', 'r')
prime = key.readline()
if prime == "!<--!http://skl-trade.ru/http://skl-trade.ru/http://skl-trade.ru/!-->!":
    print('Запускаю библиотеки...')
    f = open("data/settings.txt", "r")
    url_M = f.readline()
    all_products = []
    type_product = ["qnap", 'oborudovaniye-zyxel', 'oborudovaniye-spanzyxel-span', 'panasonic', 'oborudovaniye-spanzyxel-span-1', 'videonablyudeniye-spanpelco-span',
    'videonablyudeniye-spanaxis-span', 'istochniki-pitaniya-spanskat-bastion-span', 'videonablyudeniye-spandahua-span', 'videonablyudeniye-spanrvi-span',
    'istochniki-pitaniya-spanskat-bastion-span']
    dost = requests.get(url_M)
    print('Доступ к сайту <-> ' + str(dost))
    print('HTML разметка сайта получена')
    print('Количество каталогов -> 11')
    process = 0
    print('Начинаю парсинг товаров для сравнения: \n')
    for konstruktor in type_product:
        print(f'Процесс парсинга -> {round(process/11*100)}%')
        process += 1
        url_1 = str(url_M + "magazin/folder/" + konstruktor)
        html = requests.get(url_1).text
        soup = BeautifulSoup(html, 'html.parser')
        vallue_str = soup.find("li", class_='page-last').a['href']
        url_2 = str(url_M + vallue_str)
        html_1 = requests.get(url_2).text
        last_str_pre = BeautifulSoup(html_1, 'html.parser')
        last_str = int(last_str_pre.find("li", class_='page-num active-num').span.text)
        for i in range(last_str):
            konstr = url_M + "magazin/folder/" + konstruktor + "/p/" + str(i)
            request = requests.get(konstr).text
            soup_3 = BeautifulSoup(request, 'html.parser')
            name = soup_3.find("div", class_='product-name').a.text
            counts = soup_3.find('div', class_='price-current').strong.text.split()
            i = 1
            coun = str()
            for count in counts:
                coun += str(count)
            all_products.append({
            'NAME': name,
            'COUNT': coun,
            })
    for all_product in all_products:
        pr_s =+ 1
    print(f'Количество товаров -> {pr_s}')
    print("""Парсинг успешен!
    Начинаю запись в XLSX документ: """)
    save = xlsxwriter.Workbook('data/Save Information.xlsx')
    list = save.add_worksheet()
    list.write('A1', "Наименнование товара")
    list.write('B1', "Наша цена")
    stroka = 2
    for all_product in all_products:
        print(f'Запись в XLSX документ -> {round(stroka/pr_s)}')
        list.write('A' + str(stroka), all_product['NAME'])
        list.write('B' + str(stroka), all_product['COUNT'])
        stroka += 1
    save.close()
    print("Запись в XLSX файл завершена. Просмотреть данные можно в каталоге data -> Save Information.xlsx")
else:
    print('Ключ не найдет')
exit = input('Теперь можете закрыть данное окно!')
