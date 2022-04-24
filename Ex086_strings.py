'''
Предложите пользователю ввести пароль, а затем предложите ввести его повторно. 
Если два пароля совпадут, выведите сообщение «Thank you». 
Если буквы введены правильно, но различаются регистром, выведите сообщение «They must be in the same case»;
в противном случае выводится сообщение «Incorrect».
'''

pass1 = input('Enter the password: ')
pass2 = input('Enter the password again: ')
if pass1 == pass2:
    print('Thank you!')
elif pass1.lower() == pass2.lower():
    print('They must be in the same case')
else:
    print('incorrect')

    