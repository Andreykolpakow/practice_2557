from requests import get, utils
from datetime import date

def currency_rates(valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    day, month, year = (content[content.find('Date=') + 6:content.find('Date=') + 16]).split('.')
    currency_day = date(int(year), int(month), int(day))

    val_code_index = content.find(valute.upper())
    if val_code_index < 0:
        return
    else:
        value = float(content[content.find('Value', val_code_index)+6:content.find('Value', val_code_index)+13].\
            replace(',', '.'))
        return f'{value}, {currency_day}'