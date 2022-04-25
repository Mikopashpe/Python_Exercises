'''
Используя двумерный список из задачи 096, предложите пользователю выбрать строку и выведите только ее. 
Предложите ввести новое значение, добавьте его в конец строки, после чего снова выведите измененную строку.
'''

new_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

user_ind = int(input('Enter the number of list: ')) - 1
print(new_list[user_ind])

usernum = int(input('Enter new element: '))
new_list[user_ind].append(usernum)
print(new_list[user_ind])

