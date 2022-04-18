'''
Предложите пользователю ввести радиус и высоту цилиндра. 
Вычислите его объем (площадь круга * высота) и выведите его с точностью до трех знаков.
'''

import math


r = float(input('Enter the radius: '))
h = float(input('Enter the high: '))
S = math.pi * r**2
V = S * h
print('V =', round(V, 3))


