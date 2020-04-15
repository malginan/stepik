from selenium import webdriver
import time
import math
#============================================================================
# Задача https://stepik.org/lesson/184253/step/4?unit=158843
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)                                                 # окно №0
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]  # запомнить имя нового окна, окно №1
    browser.switch_to.window(new_window) # перейти к новому окну

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x_param = x_element.text  # считать значение Х
    # вычислить значение функции
    y = calc(x_param)
    # записать в поле input ответ
    inp_element = browser.find_element_by_id("answer")
    inp_element.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # хитрость, что бы не копировать код ответа вручную
    print(browser.switch_to.alert.text.split(': ')[-1])
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()