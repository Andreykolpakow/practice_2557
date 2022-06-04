# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
#
# Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода
# сразу для нескольких значений продолжительности, будет ли тут полезен список?

# Код для основного задания

duration = int(input('Введите время в секундах: '))
day = duration // 86400
hour = (duration - day * 86400) // 3600
min = (duration - day * 86400 - hour * 3600) // 60
sec = duration % 60

if day:
    print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')
elif hour:
    print(hour, 'час', min, 'мин', sec, 'сек')
elif min:
    print(min, 'мин', sec, 'сек')
else:
    print(sec, 'сек')


# Цикл с проверкой кода:

number_of_check = int(input('Введите количество проверок: '))
time_list = []

for i in range(number_of_check):
    duration = int(input('Введите время в секундах: '))
    day = duration // 86400
    hour = (duration - day * 86400) // 3600
    min = (duration - day * 86400 - hour * 3600) // 60
    sec = duration % 60

    if day:
        time_list.append(f'{day} дн, {hour} час, {min} мин, {sec} сек')
    elif hour:
        time_list.append(f'{hour} час, {min} мин, {sec} сек')
    elif min:
        time_list.append(f'{min} мин, {sec} сек')
    else:
        time_list.append(f'{sec} сек')

print(time_list)