from selenium import webdriver
import time
import math
# ============================================================================
# Задача https://stepik.org/lesson/184253/step/4?unit=158843
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
