'''
Предложите пользователю ввести названия четырех любимых блюд и сохраните их в словаре с числовыми индексами, начиная с 1. 
Выведите содержимое словаря с указанием индексов и элементов. 
Спросите пользователя, какой элемент он хочет исключить, и удалите его из списка. 
Отсортируйте оставшиеся данные и выведите содержимое словаря.
'''

l1 = [1, 2, 3, 4]
f1 = input('Enter the 1st food: ')
f2 = input('Enter the 2nd food: ')
f3 = input('Enter the 3rd food: ')
f4 = input('Enter the 4th food: ')
l2 = [f1, f2, f3, f4]
new_dict = dict(zip(l1, l2))
print(new_dict)
user_choise = int(input('What food do you wanna to remove from the dict? Enter the number: '))
del new_dict[user_choise]
print(new_dict)

