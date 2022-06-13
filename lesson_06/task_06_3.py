# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель
# между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них
# словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во
# много раз меньше объема ОЗУ.

# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович

# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

import os.path

with open(os.path.join('task_3', 'task_3_users.csv'), 'r', encoding='utf-8') as names:
    names_list = [' '.join(name.rstrip().split(',')) for name in names]
    # print(names_list)

with open(os.path.join('task_3', 'task_3_hobby.csv'), 'r', encoding='utf-8') as hobbyes:
    hobbyes_list = [hobby.rstrip().replace(',', ', ') for hobby in hobbyes]
    # print(hobbyes_list)

if len(names_list) <= len(hobbyes_list):
    result_dict = {names_list[i]: hobbyes_list[i] for i in range(len(names_list))}
    with open(os.path.join('task_3', 'res_dict.txt'), 'w', encoding='utf-8') as f:
        f.write(str(result_dict))
    with open(os.path.join('task_3', 'res_dict.txt'), 'r', encoding='utf-8') as f:
        print('В файле записано:\n', f.read())
    exit(1)
elif len(names_list) > len(hobbyes_list):
    result_dict = {names_list[i]: hobbyes_list[i] if i < len(hobbyes_list) else None for i in range(len(names_list))}
else:
    print('Проверь условия. Где-то ошибка')

with open(os.path.join('task_3', 'res_dict.txt'), 'w+', encoding='utf-8') as f:
    f.write(str(result_dict))
with open(os.path.join('task_3', 'res_dict.txt'), 'r', encoding='utf-8') as f:
    print('В файле записано:\n', f.read())