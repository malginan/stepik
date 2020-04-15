from selenium import webdriver
import time
import math
#============================================================================
# Задача https://stepik.org/lesson/184253/step/4?unit=158843
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # # вызвать окно с сообщением и кнопкой ОК с помощью яваскрипта.
    # browser.execute_script("alert('Hello!');")
    # alert = browser.switch_to.alert # перейти в окно алерт
    # alert.accept()  # Нажать на кнопку ОК, что бы закрыть окно

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert # перейти к алерт-окну типа confirm
    confirm.accept() # нажать кнопку ОК (кно закроется)

    x_element = browser.find_element_by_id("input_value")
    x_param = x_element.text  # считать значение Х
    # вычислить значение функции
    y = calc(x_param)
    # записать в поле input ответ
    inp_element = browser.find_element_by_id("answer")
    inp_element.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()