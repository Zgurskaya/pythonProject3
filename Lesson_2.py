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
import pandas
from pprint import pprint


headers = {'User-agent': 'Mozilla/5.0 (compatible; YandexMarket/2.0; +http://yandex.com/bots)'}

def hh(main_link, search_str, n_str):
    #n_str - кол-во просматриваемых страниц
    html = requests.get(main_link+'/search/vacancy?area=22&fromSearchLine=true&st=searchVacancy&text='+search_str+'&showClusters=true',headers=headers).text
    parsed_html = bs(html,'lxml')

    jobs = []
    for i in range(n_str):
        jobs_block = parsed_html.find('div',{'class':'vacancy-serp'})
        jobs_list = jobs_block.findChildren(recursive=False)
        for job in jobs_list:
            job_data={}
            req=job.find('span',{'class':'g-user-content'})
            if req!=None:
                main_info = req.findChild()
                job_name = main_info.getText()
                job_link = main_info['href']
                salary = job.find('div',{'class':'vacancy-serp-item__compensation'})
                if not salary:
                    salary_min=None
                    salary_max=None
                else:
                    salary=salary.getText().replace(u'\xa0', u'')
                    salaries=salary.split('-')
                    salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
                    salary_min=int(salaries[0])
                    if len(salaries)>1:
                        salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
                        salary_max=int(salaries[1])
                    else:
                        salary_max=None
                job_data['name'] = job_name
                job_data['salary_min'] = salary_min
                job_data['salary_max'] = salary_max
                job_data['link'] = job_link
                job_data['site'] = main_link
                jobs.append(job_data)
        time.sleep(random.randint(1,10))
        next_btn_block=parsed_html.find('a',{'class':'bloko-button HH-Pager-Controls-Next HH-Pager-Control'})
        next_btn_link=next_btn_block['href']
        html = requests.get(main_link+next_btn_link,headers=headers).text
        parsed_html = bs(html,'lxml')

    pprint(jobs)
    return jobs

search_str='Python'
n_str=2

hh('https://vladivostok.hh.ru',search_str,n_str)
# https://vladivostok.hh.ru/search/vacancy?area=22&fromSearchLine=true&st=searchVacancy&text=Python+стажер&from=suggest_post
