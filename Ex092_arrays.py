'''
Создайте два массива: один будет содержать три числа, введенных пользователем, 
а другой — пять случайных чисел. 
Объедините эти два массива в один большой. 
Отсортируйте и выведите его, при этом каждое число должно выводиться в отдельной строке.
'''

from array import *
import random


l1 = array('i', [])
l2 = array('i', [])

for i in range(3):
    num = int(input('Enter num: '))
    l1.append(num)

for i in range(5):
    rannum = random.randint(0, 100)
    l2.append(rannum)

l2.extend(l1)
l2 = sorted(l2)
for i in l2:
    print(i)

    