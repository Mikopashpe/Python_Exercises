'''
Предложите пользователю ввести имя и фамилию в нижнем регистре. 
Преобразуйте строки к титульному регистру и соедините их. 
Выведите полученный результат.
'''



username = input('Enter your firstname: ')
username = username.capitalize()
surname = input('Enter your surname: ')
surname = surname.capitalize()
fullname = username + ' ' + surname

print(fullname)

