'''
Предложите пользователю ввести число, меньшее 20. Если введенное число больше или равно 20, 
выведите сообщение «Too high»; в противном случае выведите сообщение «Thank you».
'''

num1 = int(input('Enter the number less then 20: '))

if num1 <= 20:
    print('Thank you!')
else:
    print('Too high')

