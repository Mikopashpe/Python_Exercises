'''
Предложите пользователю ввести имя. Если длина имени меньше 5 символов, предложите ввести фамилию, 
соедините их (без пробела) и выведите полное имя в верхнем регистре. 
Если длина имени составляет 5 и более символов, выведите имя в нижнем регистре.
'''

username = input('Enter your name: ')

if len(username) < 5:
    surname = input('Enter your surname: ')
    fullname = username + surname
    print(fullname.upper())
else:
    print(username.lower())

    