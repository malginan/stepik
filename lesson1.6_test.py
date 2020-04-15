from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#============================================================================
# Задача https://stepik.org/lesson/138920/step/11?unit=196194
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    i1 = browser.find_element_by_css_selector(".first_block .first")
    i1.send_keys("Name")
    i2 = browser.find_element_by_css_selector(".first_block .second")
    i2.send_keys("MyName")
    i2 = browser.find_element_by_css_selector(".first_block .third")
    i2.send_keys("name@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()