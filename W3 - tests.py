import sys, requests

url = sys.argv[1]
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status() #генерируем исключение
except requests.Timeout:
    print('ошибка timeout', url)
except requests.HTTPError as err: #обрабатываем сгенерированное исключение
    code = err.response.status_code
    print("ошибка url: {0}, {1}".format(url, code))
except requests.RequestException: #отлавливаем базовый класс и выводим сообщение о всех прочих исключениях
    print("ошибка скачивания url: ", url)
else:
    print(response.content)
