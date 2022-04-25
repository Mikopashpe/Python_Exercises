'''
Предложите пользователю ввести пять чисел. 
Отсортируйте их и выведите для пользователя. 
Предложите выбрать одно из чисел. 
Удалите выбранное число из исходного массива и сохраните его в новом.
'''

from array import *

l1 = array('i', [])
l2 = array('i', [])

for i in range(5):
    user = int(input('Enter num: '))
    l1.append(user)
l1 = sorted(l1)
print(l1)
user_choice = int(input('Enter the num from list: '))
l1.remove(user_choice)
l2.append(user_choice)
print(l2)
print(l1)

