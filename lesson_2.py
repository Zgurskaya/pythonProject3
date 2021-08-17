# 1) Необходимо собрать информацию о вакансиях на вводимую должность(используем
# input или через анализировать несколько страниц сайта(также через input  или аргументы).Получившийся
# список должен содержать в себе минимум:
# *Наименование вакансии
# * Предлагаемую зарплату(отдельно мин.и отдельно макс.)
# *Ссылку на саму вакансию
# * Сайт откуда собрана вакансия
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
# Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести
# с помощью dataFrame через pandas. Сохраните в json либо csv.


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json

URL = 'https://vladivostok.hh.ru/search/vacancy/'
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.693 Yowser/2.5    Safari/537.36', 'accept': '*/*'
    }

def get_html(URL,params=None):
    r = requests.get(URL, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', {'data-qa': 'vacancy-serp__results'}) \
                                        .find_all('div', {'class': 'vacancy-serp-item'})

    vacancy_date = []
    for item in items:
        vacancy_date.append({
            'vacancy_name': item.find('a', {'data_qa': 'vacancy-serp__vacancy-title'}).find('span', {'class': 'resume-search-item__name'}).get_text()
        })

    print(vacancy_date)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()
