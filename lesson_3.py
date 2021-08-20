#Урок 3. Системы управления базами данных MongoDB и SQLite в Python
#1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
#записывающую собранные вакансии в созданную БД.
# 2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой
# больше введённой суммы.
# 3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)
db = client['hh_db']

vacancy_collection = db.vacancy




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_argument("--window-size=750,1080")

driver = webdriver.Chrome(executable_path='/chromedriver.exe', options=chrome_options)

driver.get("https://e.mail.ru/login?from=portal")

login = driver.find_element_by_id('user_email')
login.send_keys('study.ai_172@mail.ru')

passw = driver.find_element_by_id('user_password')
passw.send_keys('Password172')





for i in range(5):
    articles = driver.find_elements_by_class_name('gallery-list-item')
    actions = ActionChains(driver)
    actions.move_to_element(articles[-1]).key_down(Keys.ENTER)
    actions.perform()
    time.sleep(5)

passw.send_keys(Keys.ENTER)


menu = driver.find_element_by_xpath("//span[text()='РјРµРЅСЋ']")
menu.click()

but = driver.find_element_by_xpath("//button[@data-test-id='user_dropdown_menu']")
but.click()

profile = driver.find_element_by_xpath("//li/a[contains(@href,'/users/')]")
profile_url = profile.get_attribute('href')
driver.get(profile_url)

edit_profile = driver.find_element_by_class_name("text-sm")
driver.get(edit_profile.get_attribute('href'))

gender = driver.find_element_by_name('user[gender]')
select = Select(gender)

select.select_by_value('female')

gender.submit()

print()



# driver.close()


