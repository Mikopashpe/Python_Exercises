'''
Создайте список с названиями четырех телевизионных передач и выведите их на отдельных строках. 
Предложите пользователю ввести название еще одной передачи и позицию, на которой она должна быть вставлена в список. 
Снова выведите список, в котором все пять передач находятся на новых позициях.
'''

programms = ['discovery', 'netflix', 'topgear', 'NG']
for i in programms:
    print(i)
user = input('Enter the new channel: ')
user_pos = int(input('Enter the position of your channel in list: ')) - 1
programms.insert(user_pos, user)
for i in programms:
    print(i)

