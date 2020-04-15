from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#==============================================================
"""
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#time.sleep(10)
# Например, мы хотим найти кнопку со значением id="submit_button":
#button = browser.find_element_by_id("submit_button")

#Есть второй способ для поиска элементов с помощью универсального метода find_element() и полей класса By
# из библиотеки selenium.

button = browser.find_element(By.ID, "submit_button") # поиск нужной кнопки
print(button)
"""
# By.ID – поиск по уникальному атрибуту id элемента;
# By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
# By.XPATH – поиск элементов с помощью языка запросов XPath;
# By.NAME – поиск по атрибуту name элемента;
# By.TAG_NAME – поиск по названию тега;
# By.CLASS_NAME – поиск по атрибуту class элемента;
# By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
# By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.
"""
button.click() # нажать на кнопку

browser.quit() # закрыть браузер

"""
#==============================================================
#Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках,
# проще всего использовать конструкцию try/finally:
"""
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
"""
# задание  https://stepik.org/lesson/138920/step/4?unit=196194
"""
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    i1 = browser.find_element_by_name("first_name")
    i1.send_keys("Nat")
    i2 = browser.find_element_by_name("last_name")
    i2.send_keys("Ivanova")
    i3 = browser.find_element_by_class_name("city")
    i3.send_keys("Moscow")
    i4 = browser.find_element_by_id("country")
    i4.send_keys("Moscow")
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(20)
    # покажем ошибку, если возникнет
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    # обязательно закроем драйвер
finally:
    browser.quit()

"""
# задание https://stepik.org/lesson/138920/step/5?unit=196194
"""
import math
link_find = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    l = browser.find_element_by_link_text(link_find)
    l.click()
    i1 = browser.find_element_by_name("first_name")
    i1.send_keys("Nat")
    i2 = browser.find_element_by_name("last_name")
    i2.send_keys("Ivanova")
    i3 = browser.find_element_by_class_name("city")
    i3.send_keys("Moscow")
    i4 = browser.find_element_by_id("country")
    i4.send_keys("Moscow")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(20)
finally:
    browser.quit()
"""
#============================================================================
# Задание https://stepik.org/lesson/138920/step/7?unit=196194
"""
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    k = 1
    for element in elements:
        element.send_keys("Мой ответ "+str(k))
        k +=1

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
"""
#============================================================================
# https://stepik.org/lesson/138920/step/8?unit=196194
"""
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_tag_name("input")
    k = 1
    for element in elements:
        element.send_keys("Мой текст" + str(k))
        k += 1
    botton = browser.find_element_by_xpath("//button[@type='submit']")
    botton.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
"""
#============================================================================
# Задача https://stepik.org/lesson/138920/step/10?unit=196194
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
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
