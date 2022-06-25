# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество
# файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей
# (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os
import os.path

limits = [100, 1000, 10000, 100000]
folder = 'some_data'
res_dict = dict.fromkeys(limits, 0)
size_list = []
for root, dirs, files in os.walk(folder):
    for file in files:
        size_list += [os.stat(os.path.join(root, file)).st_size]

for size in size_list:
    for limit in limits:
        if size <= limit:
            res_dict[limit] += 1
            break
print(len(size_list), 'файлов')
print('\t{')
for k, v in res_dict.items():
    print('\t', f'{k}: {v}')
print('\t}')
