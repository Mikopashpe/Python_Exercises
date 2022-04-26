'''
Измените программу из задачи 098. 
Предложите пользователю выбрать строку и выведите только ее. 
Предложите выбрать столбец из выведенной строки и выведите только хранящееся там значение. 
Спросите, хочет ли пользователь изменить его. Если ответ будет положительным, 
предложите ввести новое значение и измените данные. Наконец, снова выведите измененную строку.
'''

new_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

user_ind = int(input('Enter the number of list: ')) - 1
print(new_list[user_ind])

usernum = int(input('Choose the element, enter the number: ')) - 1 

answer = input('Do you want to overwrite the number? y or n: ')
if answer == 'y':
    new_num = int(input('Enter the new number: '))
    new_list[user_ind][usernum] = new_num
    print(new_list[user_ind])
else:
    print(new_list[user_ind])


