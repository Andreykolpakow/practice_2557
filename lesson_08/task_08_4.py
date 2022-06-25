# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

def val_checker(func_checker):
    def decorator(func):
        def wrapper(x):
            if func_checker(x):
                return func(x)

            else:
                msg = f'wrong val {x}'
                raise ValueError(msg)
        return wrapper
    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(3))
print(calc_cube(-3))