from selenium import webdriver
import time
import math
# Задание https://stepik.org/lesson/228249/step/6?unit=200781

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    # считать значение переменной x
    x_element = browser.find_element_by_id("input_value")
    x_param = x_element.text

    # вычислить значение функции
    y = calc(x_param)

    # записать в поле input ответ
    inp_element = browser.find_element_by_id("answer")

    # Проскролить страницу
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp_element)
    inp_element.send_keys(y)

    # отметить чекбокс
    check_element = browser.find_element_by_id("robotCheckbox")
    check_element.click()

    # отметить радиобаттон
    radio_element = browser.find_element_by_id("robotsRule")
    radio_element.click()
    # Проскролить страницу до кнопки с помощью яваскрипта
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()