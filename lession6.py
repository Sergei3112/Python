# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

from random import uniform

n = round(uniform(1, 10), 3)


def sum_digit(n):
    return sum(map(int, list(str(n).replace('.', ''))))


print(n)
print(sum_digit(n))

# Еще одно решение, может не такое изящное как первое, но работает.
#n = input('Введите число -> ')

#suma = 0


# for digit in n:
#    if digit.isdigit():
#        suma += int(digit)


#print('Сумма ->', suma)
