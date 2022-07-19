# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

from random import randint
import math

def Get_coordinates(num_plan, left, right):     
    return tuple([randint(left, right) for i in range(num_plan)])

def Find_dist(a, b):    
    return round(math.sqrt(sum((x - y)**2 for x, y in zip(a, b))), 2)

num_plan = 2    
left = -50
right = 50

point_A = Get_coordinates(num_plan, left, right)
point_B = Get_coordinates(num_plan,left, right)

print(f'A {point_A}, B {point_B} -> {Find_dist(point_A, point_B)}')
