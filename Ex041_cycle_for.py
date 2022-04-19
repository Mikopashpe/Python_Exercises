'''
Предложите пользователю ввести имя и число. 
Если число меньше 10, программа должна вывести имя заданное количество раз; 
в противном случае она выводит сообщение «Too high» три раза.
'''


username = input('Enter your name: ')
num1 = int(input('Enter the number: '))

if num1 < 10:
    for i in range(0, num1):
        print(username)
else:
    for i in range(0, 3):
        print('Too high')

