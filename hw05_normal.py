import hw05_easy
import sys
import os
def ask_name():
    return input('введи имя директории: ')

def change_dir(name):
    if os.path.isdir(name):
        os.chdir(name)
        return 0
    else: return 1

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

while True:
    key = input('press:\n 1 - change catalog,\n 2 - list dir,\n 3 - del dir,\n 4 - create dir,\n 0 - exit')
    if   key == '0':
        sys.exit()
    elif key == '1':
        if change_dir(ask_name()):
            print('не удалось перейти')
        else:
            print('Успешно перешел')
    elif key == '2':
        hw05_easy.show_dir()
    elif key == '3':
        if hw05_easy.remove_dir(ask_name()):
            print('не удалось удалить')
        else:
            print('Успешно удалено')
    elif key == '4':
        if hw05_easy.create_dir(ask_name()):
            print('Успешно создано')
        else:
            print('не удалось создать')
    else: print('press only figures 0-4')