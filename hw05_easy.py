# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
def create_dir(name):
    ret = 0
    if os.path.isdir(name):
        print(name+' yet persists')
        ret = 1
    else:
        print('create '+name)
        ret = os.mkdir(name)
    return ret

def remove_dir(name):
    ret = 0
    if os.path.isdir(name):
        print('remove '+name)
        os.rmdir(name)
    else:
        print(name+' not persists')
        ret = 1
    return ret

def show_dir():
    lst = os.listdir()
    for el in lst:
        if os.path.isdir(el): print(el)




input('press ENTER, task easy 1,2')
for i in range(1,10):
    name_dir = 'dir_'+str(i)
    if create_dir(name_dir): break

show_dir()

for i in range(1,10):
    name_dir = 'dir_'+str(i)
    if remove_dir(name_dir): break

show_dir()

input('press ENTER, next: task easy 3')

import sys
import shutil

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
fullname = sys.argv[0]
name     = os.path.basename(fullname)
lst      = os.path.splitext(name)
new_name = lst[0]+'_copy'+lst[1]
shutil.copyfile(name,new_name)

