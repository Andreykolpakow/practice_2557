# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную
# работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

num_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

num = input('Введите число: ')


def num_translate_adv(num):
    if 'A' <= num[0] <= 'Z':
        return num_dict.get(num.lower()).capitalize()
    else:
        return num_dict.get(num.lower())


print('"', num_translate_adv(num), '"', sep='')
