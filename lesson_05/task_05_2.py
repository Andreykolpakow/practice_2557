# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield.


n = int(input('До какого числа сгенерировать? '))
gen_without_yield = (x for x in range(1, n+1, 2))

print(gen_without_yield)
print(type(gen_without_yield))
print(*gen_without_yield)