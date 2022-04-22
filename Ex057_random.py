'''
Измените программу 056 так, чтобы перед повторным предположением она сообщала пользователю, 
является ли его предположение больше или меньше загаданного числа.
'''

import random    

num = random.randint(1, 10)    
usernum = int(input('Enter the number from 1 to 10: '))    

while num != usernum:
    if usernum > num:
        print('Too high')  
    elif usernum < num:
        print('Too low')  
    usernum = int(input('No, try again: '))    
print('Correct!')    

