'''
Предложите пользователю ввести значение 1, 2 или 3. 
Если введено значение 1, выведите сообщение «Thank you»; 
если 2 — сообщение «Well done»; 
если 3 — сообщение «Correct». 
Если введено любое другое значение, выведите сообщение «Error message».
'''

num1 = int(input('Enter the number: '))


if num1 == 1:
    print('Thank you')
elif num1 == 2:
    print('Well done')
elif num1 == 3:
    print('Correct')
else:
    print('Error message')


