'''
Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. 
Если будет введено число меньше 10, запросите имена и после каждого имени выведите строку 
«[имя] has been invited». 
Если введенное число больше или равно 10, выведите сообщение «Too many people».
'''

people = int(input('How many people will be? '))


if people < 10:
    for i in range(0, people):
        names = input('Name of guest ')
        print(names, 'has been invited')
elif people >= 10:
    print('Too many people')

    