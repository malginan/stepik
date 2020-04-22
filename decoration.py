def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func("123")
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world(x):
    print('Hello world!', x)

hello_world()