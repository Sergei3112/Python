# Sympy:
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1 Определить корни
# 2 Найти интервалы, на которых функция возрастает
# 3 Найти интервалы, на которых функция убывает
# 4 Построить график
# 5 Вычислить вершину
# 6 Определить промежутки, на котором f > 0
# 7 Определить промежутки, на котором f < 0

import sympy
import matplotlib as plt
from sympy import symbols, plot_parametric
from sympy.plotting import plot
from sympy.solvers import solve


x = symbols('x')


plot(((-12)*sympy.sin(sympy.cos(x))*x**4 - 18 *
     (x**3)+5*(x**2) + 10*x - 30), (x, -50, 50))
