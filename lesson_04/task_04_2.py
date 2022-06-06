# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю. Использовать
# библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать
# результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами
# использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции
# не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.


from requests import get, utils


def currency_rates(valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    val_code_index = content.find(valute.upper())
    if val_code_index < 0:
        return
    else:
        value = float(content[content.find('Value', val_code_index)+6:content.find('Value', val_code_index)+13].\
            replace(',', '.'))
        return value


print(currency_rates('aud'))
print(currency_rates('USD'))
print(currency_rates('EUr'))
print(currency_rates('gbP'))
print(currency_rates('ByN'))

