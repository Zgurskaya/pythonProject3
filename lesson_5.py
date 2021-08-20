# Урок 5. Scrapy
# 1) Написать программу, которая собирает входящие письма из своего или тестового почтового
# ящика и сложить данные о письмах в базу данных (от кого, дата отправки, тема письма, текст
# письма полный)
# Логин тестового ящика: study.ai_172@mail.ru
# Пароль тестового ящика: NextPassword172!!!
#
# 2) Написать программу, которая собирает «Новинки» с сайта техники mvideo и складывает
# данные в БД. Сайт можно выбрать и свой. Главный критерий выбора: динамически загружаемые
# товары

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_argument("--window-size=750,1080")

driver = webdriver.Chrome(executable_path='C:\\Users\\1\PycharmProjects\pythonProject3\chromedriver.exe', options=chrome_options)

driver.get("https://mail.ru")

login = driver.find_element_by_class_name('email-input')
login.send_keys('study.ai_172@mail.ru')

button = driver.find_element_by_class_name('button')
button.send_keys(Keys.ENTER)
passw = driver.find_elements_by_name("password")
passw.send_keys('NextPassword172!!!')
passw.send_keys(Keys.ENTER)





