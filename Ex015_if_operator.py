'''
Предложите пользователю ввести любимый цвет. Если он введет «red», «RED» или «Red», 
выведите сообщение «I like red too». В противном случае выведите сообщение «I don’t like [colour], I prefer red».
'''

color = input('What is your favorite color? ')


if color == 'red' or color == 'Red' or color == 'RED':
    print('I like red too')
else:
    print('I do not like', color, 'I prefer red')

    