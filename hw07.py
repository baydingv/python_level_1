#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import os
import random

class Table():
    Nx,Ny,Nn = 9,3,5
    ix = list(range(Nx))
    def __init__(self, N_keg, name):
        self.my_name = name
        self.i1 = random.sample(self.ix,self.Nn); self.i1.sort()
        self.i2 = random.sample(self.ix,self.Nn); self.i2.sort()
        self.i3 = random.sample(self.ix,self.Nn); self.i3.sort()
        bag = ['%2s' %e for e in range(1, N_keg+1)]
        random.shuffle(bag)
        n = self.Nn
        self.v1 = bag[0:n]; self.v2 = bag[n:2*n]; self.v3 = bag[2*n:3*n]
        self.v1.sort(); self.v2.sort(); self.v3.sort()
        self.n_rest = 3*self.Nn

    def __str__(self):
        sm = [self.i1[0],self.i1[1]-self.i1[0]-1,self.i1[2]-self.i1[1]-1,self.i1[3]-self.i1[2]-1,self.i1[4]-self.i1[3]-1]
        s1 = '   '*sm[0]+'%2s '+'   '*sm[1]+'%2s '+'   '*sm[2]+'%2s '+'   '*sm[3]+'%2s '+'   '*sm[4]+'%2s '
        sm = [self.i2[0],self.i2[1]-self.i2[0]-1,self.i2[2]-self.i2[1]-1,self.i2[3]-self.i2[2]-1,self.i2[4]-self.i2[3]-1]
        s2 = '   '*sm[0]+'%2s '+'   '*sm[1]+'%2s '+'   '*sm[2]+'%2s '+'   '*sm[3]+'%2s '+'   '*sm[4]+'%2s '
        sm = [self.i3[0],self.i3[1]-self.i3[0]-1,self.i3[2]-self.i3[1]-1,self.i3[3]-self.i3[2]-1,self.i3[4]-self.i3[3]-1]
        s3 = '   '*sm[0]+'%2s '+'   '*sm[1]+'%2s '+'   '*sm[2]+'%2s '+'   '*sm[3]+'%2s '+'   '*sm[4]+'%2s '
        ln = len(self.my_name); lh1 =(26-ln)//2; lh2=26-ln-lh1; sh = '-'*lh1 + self.my_name +'-'*lh2; sf = '-'*26
        sret = ''.join([sh,'\n',s1,'\n',s2,'\n',s3,'\n',sf])
        vret = tuple(self.v1+self.v2+self.v3)
        return sret%vret

    def clear(self,num):
        k = '%2s' % (num)
        do = True
        if k in self.v1:
            i = self.v1.index(k)
            self.v1.pop(i)
            self.v1.insert(i,' -')
        elif k in self.v2:
            i = self.v2.index(k)
            self.v2.pop(i)
            self.v2.insert(i,' -')
        elif k in self.v3:
            i = self.v3.index(k)
            self.v3.pop(i)
            self.v3.insert(i,' -')
        else:
            do = False
        self.n_rest = 15 - (self.v1.count(' -') + self.v2.count(' -') + self.v3.count(' -'))
        return self.n_rest, do

class Bag():
    def __init__(self, my_N):
        self.bag = list(range(1, my_N+1))
        random.shuffle(self.bag)
    def get_out_keg(self):
        lb = len(self.bag)
        if lb < 1: ret=[0,0]
        else:      ret=[self.bag.pop(), lb - 1]
        return ret

# ------ M A I N ----------------------------------------------------
N = 90
BG = Bag(N)
T1 = Table(N, 'Моя карточка')
T2 = Table(N, 'Карточка компьютера')
n1,n2 = 15,15                           # текущее количество незакрытых полей на каждой карточке
while N:
    os.system('cls')
    print('      <<< МОЁ ЛОТО >>>')
    print(T1)
    print('')
    print(T2)
    [k,N] = BG.get_out_keg()
    ans = input('№ %d, (осталось бочонков %d), зачеркнуть поле? <y/n/q>: ' % (k,N))
    if ans == 'q': break
    n1,do = T1.clear(k)
    if do and ans != 'y' or not do and ans == 'y':
        print('Я проиграл...')
        break
    n2,do = T2.clear(k)
    print('')

    if not n1 and n2: print('Я выиграл !!!');break
    if not n2 and n1: print('Я проиграл...');break
input('конец игры  -  жми <ENTER>')
