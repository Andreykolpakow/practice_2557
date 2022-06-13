# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield,
# например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...


def gen(n):
    i = 1
    while i <= n:
        yield i
        i += 2

# gen_15 = gen(15) # Для истощения генератора в консоли вручную
# next(gen_15)

# for i in gen(25): # Для истощения генератора в самой программой
#     print(i)