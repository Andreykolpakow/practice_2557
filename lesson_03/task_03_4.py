# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых
# фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv(*args):
    res_dict = {}
    family_dict = {}
    for name in args:
        family_litera = name.split()[-1][0]
        if family_litera not in family_dict:
            family_dict[family_litera] = [name]
        else:
            family_dict[family_litera].append(name)


    for key, names in family_dict.items():
        name_dict = {}
        for name in names:
            if name[0] not in name_dict:
                name_dict[name[0]] = [name]
            else:
                name_dict[name[0]].append(name)
            res_dict[key] = name_dict
    return res_dict


# Вывод словаря в одну строку:
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                    "Семён Слепаков"), '\n')

# Вывод словаря построчно:
result_dict_global = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                    "Семён Слепаков")
print('{')
for family, names in result_dict_global.items(): # Вывел построчно
    print('\t', f'"{family}":', '{')
    for litera, name in names.items():
        print('\t', '\t', f'"{litera}": {name}')
    print('\t', '}')
print('}')

