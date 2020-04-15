import time
from selenium import webdriver # webdriver это и есть набор команд для управления браузером
driver = webdriver.Chrome()  # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

time.sleep(5)  # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(15)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)


# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
