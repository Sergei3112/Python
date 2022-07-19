# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

from random import randint

quarter = randint(1, 4)
diapasones = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']

def show_diapasone (quart, diapasones):
    return diapasones[quart-1]

print (f'четверть -> {quarter}') 
print(f'возможные координаты четверти -> {diapasones[quarter-1]}')