# Реализуйте алгоритм перемешивания списка.

import random
lst = [random.randint(0,5) for i in range(random.randint(1,10))]
print(f'исходный список: -> {lst}')
random.shuffle(lst)
print(f'список после перемешивания -> {lst}')

