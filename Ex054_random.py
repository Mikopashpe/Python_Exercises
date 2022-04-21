'''
Случайным образом выберите «орел» или «решку» ("h" или "t"). 
Предложите пользователю угадать ваш выбор. 
Если ваш выбор совпадает со случайно выбранным значением, выведите сообщение «You win»; 
в противном случае выведите сообщение «Bad luck». 
В конце сообщите пользователю, какое значение было загадано — «орел» или «решка».
'''

import random
from secrets import choice

choice = ['h', 't']
u = random.choice(choice)
answer = input('Heads or tails? ')
if answer == u:
    print('You win')
else:
    print('Bad luck\nMy choice is', u)

    
