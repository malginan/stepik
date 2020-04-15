from selenium import webdriver
import time
import math
#============================================================================
# Задача https://stepik.org/lesson/165493/step/5?unit=140087
"""
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # считать значение переменной x
    x_element = browser.find_element_by_id("input_value")
    x_param = x_element.text
    # вычислить значение функции
    y = calc(x_param)
    # записать в поле input ответ
    inp_element = browser.find_element_by_id("answer")
    inp_element.send_keys(y)
    #time.sleep(5)
    # отметить чекбокс
    check_element = browser.find_element_by_id("robotCheckbox")
    check_element.click()
    # отметить радиобаттон
    radio_element = browser.find_element_by_id("robotsRule")
    radio_element.click()
    #time.sleep(5)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
"""
#============================================================================
# Задача https://stepik.org/lesson/165493/step/7?unit=140087
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # считать значение переменной Х из значения атрибута
    x_element = browser.find_element_by_id("treasure")
    x_param = x_element.get_attribute("valuex")
    print('x_param ',x_param)
    # вычислить значение функции
    y = calc(x_param)
    # записать в поле input ответ
    inp_element = browser.find_element_by_id("answer")
    inp_element.send_keys(y)

    # так можно проверить, отмечен ли радиобаттон(это не по задаче)
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    # конец проверки

    # отметить чекбокс
    check_element = browser.find_element_by_id("robotCheckbox")
    check_element.click()
    # отметить радиобаттон
    radio_element = browser.find_element_by_id("robotsRule")
    radio_element.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()