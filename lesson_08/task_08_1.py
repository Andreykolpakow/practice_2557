# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
#
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
# выражении; имеет ли смысл в данном случае использовать функцию re.compile()?

import re

RE_EMAIL = re.compile(r"(?P<username>\w*['+-\.]?\w*)@(?P<domain>\w+[-\.]*\w*\.+\w*)")


def email_parse(email):
    try:
        re_match = RE_EMAIL.match(email)
        # return {'username': re_match.group('username'), 'domain': re_match.group('domain')}
        return re_match.groupdict()
    except AttributeError:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))