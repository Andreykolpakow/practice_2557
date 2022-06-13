# Для чтения данных реализовать в командной строке
# следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

from sys import argv

read_param = argv[:]

if len(read_param) > 3:
    exit('Введите корректные данные')

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(read_param) == 1:
        print(f.read())
    elif len(read_param) == 2:
        i = 1
        for line in f:
            if i >= int(argv[1]):
                print(line.rstrip())
            i +=1
    elif len(read_param) == 3:
        i = 1
        for line in f:
            if int(argv[2]) >= i >= int(argv[1]):
                print(line.rstrip())
            i += 1