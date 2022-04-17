'''
Предложите пользователю ввести число. 
Если оно меньше 10, выведите сообщение «Too low»; 
если число лежит в диапазоне от 10 до 20 — сообщение «Correct». 
В остальных случаях выведите сообщение «Too high».
'''

num1 = int(input('Enter the number: '))


if num1 < 10:
    print('Too low')
elif 10 <= num1 <= 20:
    print('Correct')
else:
    print('Too high')

