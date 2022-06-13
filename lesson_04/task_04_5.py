# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05


# from datetime import date
# from requests import get, utils
# import sys


# def currency_rates(argv):
#
#     response = get('http://www.cbr.ru/scripts/XML_daily.asp')
#     encodings = utils.get_encoding_from_headers(response.headers)
#     content = response.content.decode(encoding=encodings)
#
#     day, month, year = (content[content.find('Date=')+6:content.find('Date=')+16]).split('.')
#     currency_day = date(int(year), int(month), int(day))
#
#     # _, *args = argv
#     valute = sys.argv[1]
#     print(valute)
#
#     val_code_index = content.find(str(valute.upper()))
#     if val_code_index < 0:
#         print('Нет такой валюты')
#     else:
#         value = float(content[content.find('Value', val_code_index)+6:content.find('Value', val_code_index)+13].\
#             replace(',', '.'))
#         print(value, currency_day)

# if __name__ == '__main__':
#     import sys


import sys
from utils import currency_rates

valutes = sys.argv[1:]

for code in valutes:
    print(code, currency_rates(code))


# import sys
# from datetime import date
# from requests import get, utils
#
#
# def currency_rates(valute):
#     response = get('http://www.cbr.ru/scripts/XML_daily.asp')
#     encodings = utils.get_encoding_from_headers(response.headers)
#     content = response.content.decode(encoding=encodings)
#
#     day, month, year = (content[content.find('Date=')+6:content.find('Date=')+16]).split('.')
#     currency_day = date(int(year), int(month), int(day))
#
#     val_code_index = content.find(valute.upper())
#     if val_code_index < 0:
#         return
#     else:
#         value = float(content[content.find('Value', val_code_index)+6:content.find('Value', val_code_index)+13].\
#             replace(',', '.'))
#         return f'{value}, {currency_day}'
#
# arg = sys.argv[1:]
# for i in arg:
#     a = currency_rates(i)
#     print(a)