'''
Используя двумерный список из задачи 096, предложите пользователю выбрать 
строку и столбец и выведите выбранное значение.
'''



new_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]


for i in new_list:
    print(i)

user_ind = int(input('Enter the number of list: ')) - 1
user_el = int(input('Enter the element: ')) - 1

print(new_list[user_ind][user_el])

