# Eсли нам понадобится загрузить файл на веб-странице
import os
from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    i1 = browser.find_element_by_name("firstname")
    i1.send_keys("Name")
    i2 = browser.find_element_by_name("lastname")
    i2.send_keys("MyName")
    i2 = browser.find_element_by_name("email")
    i2.send_keys("name@mail.ru")

""""
# Нашёл довольно красивый способ сразу заполнить все импорты:

for inp in browser.find_elements_by_css_selector(".form-group input"):
    inp.send_keys("data")
"""

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'qwe.txt')           # добавляем к этому пути имя файла
    element  = browser.find_element_by_css_selector("[type='file']")
    #element.click()
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()