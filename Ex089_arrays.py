'''
Создайте массив для хранения целых чисел. 
Сгенерируйте пять случайных чисел и сохраните их в массиве. 
Выведите массив (каждый элемент должен выводиться в отдельной строке).
'''

import random
from array import *

new_list = array('i', [])

for i in range(5):
    num = random.randint(0, 100000)
    new_list.append(num)
    print(new_list[i])
