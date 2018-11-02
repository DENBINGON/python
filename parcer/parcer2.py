import tkinter as tk
from bs4 import BeautifulSoup, SoupStrainer
import requests

URL1 = "https://www.gelbeseiten.de/apotheken/berlin"
URL_end = "https://www.gelbeseiten.de/apotheken/berlin/s1000"
pars = []
links = []
html_end = requests.get(URL_end).text
soup_end = BeautifulSoup(html_end, 'html.parser')
ul_end = soup_end.find("div", class_="gs_paginierung__inner-wrapper")
end_all = int(ul_end.find_all("li")[-1].text)
for list in range(end_all):
    if list == 0:
        list = 1
    URL = str(URL1) + '/s' + str(list)
    print(f'Parsing: {list} => {end_all} = {round(list/end_all*100)}%')
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'html.parser')
    div_all = soup.find("div", id="gs_treffer")
    for row in div_all.find_all("div", class_="name m08_name"):
        for link in row.find_all('a', class_="m08_teilnehmername teilnehmername entry", href=True):
            links.append({"LINK": link['href']})
            url_link = link['href']
            html_link = requests.get(url_link).text
            soup_html_link = BeautifulSoup(html_link, 'html.parser')
            all_div_link = soup_html_link.find("div", class_="center-column")
            NAME = all_div_link.find("h1", class_="mod-TeilnehmerKopf__name").text
            ADDRES_D = all_div_link.find("div", class_="mod mod-Kontaktdaten")
            for i in range(2):
                ADDRES = ADDRES_D.find("p").text    #может потребоваться .find_all
            PHONE = all_div_link.find("a", class_="nolink-black")
            EMAIL_D = all_div_link.find("li", class_="mod-Kontaktdaten__list-item :: link-blue")
            EMAIL = EMAIL_D.find("span").text
        pars.append({
            'NAME': NAME,
            'ADDRES': ADDRES,
            'PHONE': PHONE.span.text,
            'EMAIL': EMAIL,
        })
for par in pars:
    print(par)
