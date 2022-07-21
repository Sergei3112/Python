# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

n = int(input('Введите число: '))


def feb_print(n):
    list_1 = [0]
    feb1 = 1
    feb2 = 0
    for i in range(n):
        feb1, feb2 = feb2, feb1+feb2
        list_1.append(feb2)
        list_1.insert(0, ((-1) ** (i) * feb2))
    print(list_1)


feb_print(n)
