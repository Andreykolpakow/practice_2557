# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses
# меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None),
# например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать,
# в каких ситуациях генератор даст эффект.

# Вариант 1. Не уверен, что zip - это именно генератор. Но на списках, когда учеников меньше, чем классов, работает
# в нужном формате

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

zip_gen = zip(tutors, klasses)
print(type(zip_gen))
try:
    for i in range(len(tutors)):
        print(next(zip_gen))
except StopIteration:
    print('Генерация закончилась исключением StopIteration', '\n')

# Вариант 2.

g = ((tutors[i], klasses[i] if i < len(klasses) else None) for i in range(len(tutors)))

print('\n', type(g))
for tupl in g:
    print(tupl)


