# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если,
# например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка
# после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав
# минимум кода?

pricelist = [57.8, 46.51, 97, 1.01, 10.5, 20.55, 32.99, 48, 73.15, 100]

for price in pricelist:
    rub = int(price)
    kop = int(round(price % 1 * 100, 2))
    print(f'{rub} руб {kop:02d} коп, ', end='')

print('\nid изначального списка: ', id(pricelist))
print('Цены по возрастанию:')
pricelist.sort()
print(pricelist)
print('id отсортированного списка: ', id(pricelist))
price_down_list = sorted(pricelist, reverse=True)
print('Цены по убыванию:')
print(price_down_list)
print('id нового списка: ', id(price_down_list))

print('Пять самых дорогих товаров: ')
print(price_down_list[4::-1])