from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
#============================================================================
# Задача https://stepik.org/lesson/184253/step/4?unit=158843
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    #button = browser.find_element_by_id("verify")

    # говорим Selenium проверять в течение 12 секунд, текст (в элементе h5 с id="price")  не станет $100
    # используем специальный модуль expected_conditions, называя его EC
    pryce = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x_param = x_element.text  # считать значение Х
    # вычислить значение функции
    y = calc(x_param)
    # записать в поле input ответ
    inp_element = browser.find_element_by_id("answer")
    inp_element.send_keys(y)

    button = browser.find_element_by_css_selector(".form-group button.btn")
    button.click()

    # хитрость, что бы не копировать код ответа вручную
    #print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()