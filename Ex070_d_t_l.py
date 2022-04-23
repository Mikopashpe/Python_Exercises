'''
Доработайте программу 069 так, чтобы она предлагала пользователю ввести число 
и выводила название страны, находящейся в заданной позиции.
'''

countries = ('Germany', 'France', 'Georgia', 'UK', 'Litva')
print(countries)
user_choice = int(input('Choose the number: '))
print('Country of', user_choice, 'index is', countries[user_choice])

