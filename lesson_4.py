# 1. Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex - новости.
# Для парсинга использовать XPath.Структура данных должна содержать:
# * название источника;
# * наименование новости;
# * ссылку на новость;
# * дата публикации.
# 2. Сложить собранные данные в БД. Минимум один сайт, максимум - все три/

from lxml import html
import requests
from datetime import datetime
from pprint import pprint


header = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.693 Yowser/2.5    Safari/537.36'
}

link_lenta_ru = 'https://lenta.ru/'
response = requests.get(link_lenta_ru, headers=header)
dom = html.fromstring(response.text)

news = dom.xpath('''//section[@class="row b-top7-for-main js-top-seven"]//div[contains(@class,'item')]''')
new_list = []
for new in news:
    new_data = {}
    new_title = new.xpath(".//a//text()")
    new_link = new.xpath(".//a//@href")
    for i in range(len(new_data)):
        new_data[i] = new_data[i].replace(u'\xa0', u' ')

    new_data['new_title'] = new_title
    new_data['new_link'] = new_link


    new_list.append(new_data)

pprint(new_list)

