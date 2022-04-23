'''
Создайте список с названиями двух видов спорта. 
Предложите пользователю ввести свой любимый вид спорта и добавьте его в конец списка. 
Отсортируйте список и выведите его.
'''

sportlist = ['tennis', 'swimming']
user_sport = input('Enter your favorite sport: ')
sportlist.append(user_sport)
sportlist.sort()
print(sportlist)

