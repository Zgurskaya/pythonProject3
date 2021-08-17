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

from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
import json

def _parser_hh(vacancy):
    vacancy_date = []

    params = {
        'text': vacancy,
        'search_field': 'name',
        'items_on_page': '100',
        'page': ''
    }

    URL = 'https://vladivostok.hh.ru/search/vacancy/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.693 Yowser/2.5    Safari/537.36', 'accept': '*/*'
    }
    html = requests.get(URL, params=params, headers=HEADERS)

    if html.ok:
        parsed_html = bs(html.text, 'html.parser')

        page_block = parsed_html.find('div', {'data-qa': 'pager-block'})
        if not page_block:
            last_page = '1'

        else:
            last_page = int(page_block.find_all('div', {'id': 'HH-React-Root'})[-1].getText())


    for page in range(0, last_page):
        params['page'] = page
        html = requests.get(URL, params=params, headers=HEADERS)

        if html.ok:
            parsed_html = bs(html.text, 'html.parser')

            vacancy_items = parsed_html.find('div', {'data-qa': 'vacancy-serp__results'}) \
            .find_all('div', {'class': 'vacancy-serp-item'})

            for item in vacancy_items:
                vacancy_date.append(_parser_item_hh(item))

    return vacancy_date


def _parser_item_hh(item):
    vacancy_date = {}

    # vacancy_name
    vacancy_name = item.find('span', {'class': 'resume-search-item__name'}) \
        .getText() \
        .replace(u'\xa0', u' ')

    vacancy_date['vacancy_name'] = vacancy_name

    # company_name
    company_name = item.find('div', {'class': 'vacancy-serp-item__meta-info-company'}) \
        .find('a') \
        .getText()

    vacancy_date['company_name'] = company_name

    # city
    city = item.find('span', {'class': 'vacancy-serp-item__meta-info'}) \
        .getText() \
        .split(', ')[0]

    vacancy_date['city'] = city

    # salary
    salary = item.find('div', {'class': 'vacancy-serp__vacancy-compensation'})
    if not salary:
        salary_min = None
        salary_max = None
        salary_currency = None
    else:
        salary = salary.getText() \
            .replace(u'\xa0', u'')

        salary = re.split(r'\s|-', salary)

        if salary[0] == 'до':
            salary_min = None
            salary_max = int(salary[1])
        elif salary[0] == 'от':
            salary_min = int(salary[1])
            salary_max = None
        else:
            salary_min = int(salary[0])
            salary_max = int(salary[1])

        salary_currency = salary[2]

    vacancy_date['salary_min'] = salary_min
    vacancy_date['salary_max'] = salary_max
    vacancy_date['salary_currency'] = salary_currency

    # link
    is_ad = item.find('div', {'class': 'g-user-content'}) \
        .getText()

    vacancy_link = item.find('span', {'class': 'resume-search-item__name'}) \
        .find('a')['href']

    if is_ad != 'Реклама':
        vacancy_link = vacancy_link.split('?')[0]

    vacancy_date['vacancy_link'] = vacancy_link

    # site
    vacancy_date['site'] = 'hh.ru'

    return vacancy_date


def parser_vacancy(vacancy):
    vacancy_date = []
    vacancy_date.extend(_parser_hh(vacancy))

    df = pd.DataFrame(vacancy_date)

    return df

vacancy = 'Специалист по анализу данных'
df = parser_vacancy(vacancy)

with open('file.json', 'w') as f:
    json.dump(df.json(), f)
