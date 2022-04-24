'''
Введите список из десяти цветов. Предложите пользователю ввести начальное число в диапазоне от
0 до 4 и конечное число в диапазоне от 5 до 9. 
Выведите список цветов из интервала, заданного начальным и конечным числом.
'''

color_list = ['green', 'red', 'yellow', 'blue', 'purple', 'white', 'grey', 'black', 'orange', 'brown']
user_start = int(input('Enter the start numberfrom 0 to 4: '))
user_end = int(input('Enter the end number from 5 to 9: '))
print(color_list[user_start:user_end])


