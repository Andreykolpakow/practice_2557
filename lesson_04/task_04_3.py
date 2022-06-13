# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь
# дату из ответа, какой тип данных лучше использовать в ответе функции?

from datetime import date
from requests import get, utils


def currency_rates(valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    day, month, year = (content[content.find('Date=')+6:content.find('Date=')+16]).split('.')
    currency_day = date(int(year), int(month), int(day))
    # print(currency_day)
    # print(type(currency_day))
    val_code_index = content.find(valute.upper())
    if val_code_index < 0:
        return
    else:
        value = float(content[content.find('Value', val_code_index)+6:content.find('Value', val_code_index)+13].\
            replace(',', '.'))
        return f'{value}, {currency_day}'


print(currency_rates('aud'))
print(currency_rates('USD'))
print(currency_rates('EUr'))
print(currency_rates('gbP'))
print(currency_rates('XXX'))
