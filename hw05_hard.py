# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
#print('sys.argv = ', sys.argv)

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cd <dir_name> - переход в директорию")
    print("cp <file_name> - копирование файла")
    print("rm <file_name> - удаление файла")
    print("ls - показ пути")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def change_dir():
    name = sys.argv[2]
    if os.path.isdir(name):
        os.chdir(name)
        print('сменили директорию')
        return 0
    else:
        print('нет указанной директории')
        return 1

def copy_file():
    name = sys.argv[2]
    if os.path.isfile(name):
        lst      = os.path.splitext(name)
        new_name = lst[0]+'_copy'+lst[1]
        shutil.copyfile(name,new_name)
        print('copy file {} to {}'.format(name,new_name))
    else:
        print('нет указанного файла')
        return 1

def remove_file():
    name = sys.argv[2]
    if os.path.isfile(name):
        ans = input('подтвердите удаление файла (y/n)')
        if ans == 'y':
            os.remove(name)
            print('remove file {}'.format(name))
        else:
            print('отказ от удаления')

    elif os.path.isdir(name):
        ans = input('подтвердите удаление директории (y/n)')
        if ans == 'y':
            try:
                os.rmdir(name)
                print('remove dir {}'.format(name))
            except OSError:
                print('папка не пуста {}'.format(name))
        else:
            print('отказ от удаления')

    else:
       print('нет указанного файла')


def show_path():
    print('текущая директория: ')
    print(os.getcwd())

def ping():
    print("pong")

do = {
    "help":  print_help,
    "mkdir": make_dir,
    "cd":    change_dir,
    "cp":    copy_file,
    "rm":    remove_file,
    "ls":    show_path,
    "ping":  ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")