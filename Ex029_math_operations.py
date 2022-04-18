'''
Предложите пользователю ввести целое число больше 500. 
Вычислите квадратный корень из этого числа и выведите его с точностью до двух знаков в дробной части.
'''

import math


num1 = int(input('Enter the number over 500: '))
num2 = math.sqrt(num1)
print('Result is:', round(num2, 2))

