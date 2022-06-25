# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками»
# в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в
# родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные
# ситуации; это реальная задача, которая решена, например, во фреймворке django.


import os.path
import shutil

base_dir = 'my_project'
mother_templates = os.path.join(base_dir, 'templates')

if not os.path.exists(mother_templates):
    os.mkdir(mother_templates)

for root, dirs, files in os.walk(base_dir):
    if len(dirs) > 0:
        if dirs[0] == 'templates':
            shutil.copytree(os.path.join(root, dirs[0]), mother_templates, dirs_exist_ok=True)
