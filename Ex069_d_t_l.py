'''
Создайте кортеж с названиями пяти стран. Выведите все содержимое кортежа. 
Предложите пользователю ввести название одной из этих стран и выведите индекс (то есть позицию в списке) этого элемента кортежа.
'''

countries = ('Germany', 'France', 'Georgia', 'UK', 'Litva')
print(countries)
user_choice = input('Choose the country: ')
print('index of', user_choice, 'is', countries.index(user_choice))

