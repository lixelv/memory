import traceback

try:
    # Код, который может вызвать ошибку
    1 / 0
except Exception as e:
    # Получаем текущий трейсбек
    tb = traceback.extract_tb(e.__traceback__)
    # Получаем последний элемент трейсбека
    last_tb = tb[-1]
    # Печатаем файл, линию и текст строки кода, где произошла ошибка
    print(f"Ошибка произошла в файле {last_tb.filename} на линии {last_tb.lineno}")
    print(f"Код: {last_tb.line}")
