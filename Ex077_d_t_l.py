'''
Измените программу 076, чтобы после ввода списка имен программа выводила полный список. 
Предложите пользователю ввести одно из имен в списке и выведите позицию имени в списке. 
Спросите, хочет ли пользователь, чтобы этот человек присутствовал на вечеринке. 
Если пользователь ответит «no», удалите элемент из списка и снова выведите список.
'''

name1 = input('Enter the 1st name: ')
name2 = input('Enter the 2nd name: ')
name3 = input('Enter the 3rd name: ')
party_list = [name1, name2, name3]
answer = input('Do you wanna to invite another guest? y or n: ')
while answer == 'y':
    name = input('Enter the another guest name: ')
    party_list.append(name)
    answer = input('Do you wanna to invite another guest? y or n: ')
print(party_list)
print('You have', len(party_list), 'guests')
answer2 = input('Enter the name from list: ')
print(party_list.index(answer2))
answer3 = input('Do you wanna see this man on your party? y or n: ')
if answer3 == 'n':
    party_list.remove(answer2)
print(party_list)

