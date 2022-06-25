# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы
# вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли
# вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


def type_logger(func):
    def wrapper(*args):
        name_func = str(func).split()[1]
        res_func = func(*args)
        args_types = tuple([f'{arg}: {type(arg)}' for arg in args])
        res_arg_types = str.join(', ', args_types)
        print(f'Тип значения {name_func}:', type(res_func))
        print(f'{name_func} ({res_arg_types})')
    return wrapper


@type_logger
def calc_cube(x):
   return x ** 3

calc_cube(5)


@type_logger
def printer(*args):
    return(args)

printer('Строка', 5, 3.14, [1, 2, 3], {1:1, 2:4, 3:9})