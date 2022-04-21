'''
Выберите случайное целое число в диапазоне от 1 до 10. 
Предложите пользователю ввести число и проверьте, совпадает ли оно с загаданным. 
Продолжайте запрашивать числа до тех пор, пока пользователь не введет случайно выбранное число.
'''

import random    

num = random.randint(1, 10)    
usernum = int(input('Enter the number from 1 to 10: '))    

while num != usernum:    
    usernum = int(input('No, try again: '))    
print('Correct!')    

