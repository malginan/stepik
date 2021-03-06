# Задача https://stepik.org/lesson/36285/step/13
import unittest

from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def test_abs1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
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
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, \
                             "Failed to register on suninjuly.github.io/registration1.html")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_abs2(self):
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
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, \
                             "Failed to register on suninjuly.github.io/registration2.html")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()