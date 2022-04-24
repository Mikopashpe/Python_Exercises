'''
Выведите строку из своего любимого стихотворения и предложите пользователю ввести начальную и конечную позицию. 
Выведите символы, находящиеся между ними.
'''

my_string = 'i loved you once my love for you it maybe...'
user_start = int(input('Enter the start number: '))
user_end = int(input('Enter the end number: '))
print(my_string[user_start:user_end])

