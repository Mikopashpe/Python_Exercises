'''
Предложите пользователю ввести имена трех людей, которых он хочет пригласить на вечеринку, и сохраните их в списке. 
После того как будут введены все три числа, спросите, хочет ли пользователь добавить еще одно имя. 
Если ответ будет положительным, предложите ему добавлять имена, пока не получите ответ «no». 
После ответа «no» выведите количество людей, приглашенных на вечеринку.
'''

name1 = input('Enter the 1st name: ')
name2 = input('Enter the 2nd name: ')
name3 = input('Enter the 3rd name: ')
counter = 3
party_list = [name1, name2, name3]
answer = input('Do you wanna to invite another guest? y or n: ')
while answer == 'y':
    name = input('Enter the another guest name: ')
    counter += 1
    answer = input('Do you wanna to invite another guest? y or n: ')
else:
    print(counter)

    