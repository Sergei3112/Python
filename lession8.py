# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму


n = int(input('Введите число: '))


def get_squerence(n):
    return [round((1 + 1 / x)**x, ) for x in range(1, n + 1)]


num = get_squerence(n)
print(num)
print(round(sum(num), ))
