# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
# логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


res_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr, _, _, _, _, request_type, requested_resource, *_ = line.split()
        res_list.append((remote_addr, request_type[1:], requested_resource))

# for tup in res_list:
#     print(tup)
print(*res_list, sep='\n')

