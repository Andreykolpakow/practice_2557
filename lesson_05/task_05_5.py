# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих
# элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

from time import perf_counter

# Сформировал большой список для "утяжеления"
big_list = [num for num in range(100, 10000)]
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src.extend(big_list)
src.extend(big_list)

# Вариант 1. Через цикл
start = perf_counter()
result = []

for el in src:
    if src.count(el) == 1:
        result.append(el)

print('Вариант 1\n', result, '\n', perf_counter() - start, '\n')

# Вариант 2. Через компрехеншенс
start = perf_counter()
result = [el for el in src if src.count(el) == 1]
print('Вариант 2\n', result, '\n', perf_counter() - start, '\n')

# Вариант 3. Через множество
start = perf_counter()
result = []
tmp = set()

for el in src:
    if el not in tmp:
        result.append(el)
    else:
        if el in result:
            result.remove(el)
    tmp.add(el)

print('Вариант 3\n', result, '\n', perf_counter() - start)


