# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например,
# число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр
# которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

cube_list = [i ** 3 for i in range(1, 1000, 2)]
res_sum = 0

for cube in cube_list:
    sum_number = 0
    destr_num = cube
    while destr_num:
        sum_number += destr_num % 10
        destr_num //= 10
    if sum_number % 7 == 0:
        res_sum += cube

# Чтобы посмотреть список кубов, раскомментировать строку:
# print(cube_list)

print('Первая сумма: ', res_sum)
print('id(cube_list) = ', id(cube_list))

res_sum_2 = 0
for cube in cube_list:
    cube += 17
    sum_number = 0
    destr_num = cube
    while destr_num:
        sum_number += destr_num % 10
        destr_num //= 10
    if sum_number % 7 == 0:
        res_sum_2 += cube

print('\nНовая сумма: ', res_sum_2)
print('id(cube_list) = ', id(cube_list))
