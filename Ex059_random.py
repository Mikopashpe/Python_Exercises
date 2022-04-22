'''
Выведите названия пяти цветов, случайным образом выберите один и предложите сделать то же пользователю. 
Если пользователь выберет тот же цвет, который выбрала программа, выведите сообщение «Well done»; 
в противном случае выведите ответ, в котором скрывается намек на правильный цвет. 
Предложите пользователю повторить попытку; если пользователь и на этот раз не угадает, 
снова выведите ту же подсказку и предложите выбрать цвет (и так далее, пока пользователь не выдаст правильный ответ).
'''

import random

color_list = ['red', 'black', 'white', 'green', 'yellow']
print(color_list)
choice = random.choice(color_list)
user_choice = input('Choose the color: ')
while choice != user_choice:
    if  choice == 'red':
        print('This is color os roses')
    elif choice == 'black':
        print('This color like a darkness')
    elif choice == 'white':
        print('this color like a milk')
    elif choice == 'green':
        print('This is color of grass')
    elif choice == 'yellow':
        print('This is sun color')
    user_choice = input('Choose another color: ')
print('Well done!')

