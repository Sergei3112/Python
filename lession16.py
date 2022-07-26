# Вычислить число pi c заданной точностью d.


import math

d = '0,001'
d = int(len(d) - 2)
pi = round(math.pi, d)
print(pi)

print(f'Число Pi->{math.pi: .3f}')
