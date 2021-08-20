# 2) Написать программу, которая собирает «Новинки» с сайта техники mvideo и складывает
# данные в БД. Сайт можно выбрать и свой. Главный критерий выбора: динамически загружаемые
# товары


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

chrome_options = Options()
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)

driver.get("https://mvideo.ru/")
driver.find_element_by_class_name("c-popup__close u-sticky").click()
time.sleep(2)
