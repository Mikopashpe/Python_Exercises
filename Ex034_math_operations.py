'''
Выведите следующее сообщение:
1) Square
2) Triangle
Enter a number:
Если пользователь вводит 1, программа запрашивает длину стороны квадрата и выводит его площадь. 
Если пользователь вводит 2, программа запрашивает длину стороны и высоту треугольника, 
проведенную к этой стороне, после чего выводит его площадь. 
Если пользователь вводит что-то другое, программа должна выдать подходящее сообщение об ошибке.
'''

import math

print('1) Square\n2) Triangle')

operation = int(input('Enter a number: '))


if operation == 1:
    lenght = float(input('Enter the side lenght of a square: '))
    S_square = lenght * lenght
    print('S of a square =', S_square)
elif operation == 2:
    triangle_l = float(input('Enter the triangle lenght: '))
    triangle_h = float(input('Enter the triangle high: '))
    S_triangle = (1/2) * triangle_l * triangle_h
    print('S of a triangle =', S_triangle)
else:
    print('Please, choose the correct number of operation')

    