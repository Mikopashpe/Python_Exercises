'''
Предложите пользователю ввести его почтовый индекс. 
Выведите первые две буквы слова в верхнем регистре.
'''

ind = input('Enter your postcode: ')
letters = ind[:2]
print(letters.upper())

