'''
Выберите случайное число в диапазоне от 1 до 5. Предложите пользователю выбрать число. 
Если он угадал, выведите сообщение «Well done»; 
в противном случае сообщите, что его число больше или меньше вашего, и предложите выбрать другое число. 
Если со второго раза пользователь угадал, выведите сообщение «Correct», а если нет — сообщение «You lose».
'''

import random

num1 = random.randint(1, 5)
num2 = int(input('Choose the number from 1 to 5: '))
num3 = 0

if num1 == num2:
    print('Well done!')
elif num1 < num2:
    print('Your number is greater')
    num3 = int(input('Try again: '))
    if num3 == num1:
        print('Correct')
    else:
        print('You lose')
elif num1 > num2:
    print('My number is greater!')
    num3 = int(input('Try again: '))
    if num3 == num1:
        print('Correct')
    else:
        print('You lose')
else:
    print('Not correct')


