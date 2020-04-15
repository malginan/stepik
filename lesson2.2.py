from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#============================================================================
# Задача https://stepik.org/lesson/228249/step/3?unit=200781
try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_id("num1").text
    x2 = browser.find_element_by_id("num2").text
    y = int(x1) + int(x2)
    # инициализировать новый объект класса Select, передав в него WebElement с тегом select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(y))   # ищем элемент, в выпадающем списке, с текстом Y

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

