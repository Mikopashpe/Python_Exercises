'''
Предложите пользователю ввести число от 10 до 20 (включительно). Если будет 
введено число из этого диапазона, выведите сообщение «Thank you»; 
в противном случае выведите сообщение «Incorrect answer».
'''

num1 = int(input('Choose a number from 10 to 20: '))

if 10 <= num1 <= 20:
    print('Thank you!')
else:
    print('Incorrect answer')

