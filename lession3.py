# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

from random import randint

x = randint(-10, 10)
y = randint(-10, 10)


def get_quarter_number(x, y):
    if x != 0 and y != 0:
        if x * y > 0:
            if x > 0:
                return 1
            else:
                return 3
        else:
            if x < 0:
                return 2
            else:
                return 4
    else:
        if x == 0:
            return 'OY'
        else:
            return 'OX'


print(f' {x, y} -> {get_quarter_number(x, y)}')
