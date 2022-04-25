'''
Выведите массив из пяти чисел. 
Предложите пользователю выбрать одно из них. 
После того как число будет выбрано, выведите его позицию в массиве. 
Если пользователь введет значение, отсутствующее
в массиве, предложите ему выбрать снова, пока не будет выбрано допустимое значение.
'''

from array import *


arr = array('i', [12, 23, 34, 45, 56])
print(arr)

trig = False

while trig == False:
    user_choice = int(input('Enter the number from list: '))
    if user_choice in arr:
        print(arr.index(user_choice))
        trig = True
    else:
        print('Try again!')
    
        

 