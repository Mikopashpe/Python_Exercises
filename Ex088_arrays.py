'''
Предложите пользователю ввести пять целых чисел и сохраните их в массиве. 
Отсортируйте список и выведите его содержимое в обратном порядке.
'''

from array import *

new_list = array('i', [])
for i in range(5):
    num = int(input('Enter num: '))
    new_list.append(num)
new_list = sorted(new_list)
print(new_list)

