'''
Предложите пользователю ввести число от 1 до 12. 
Выведите таблицу умножения для этого числа.
'''

num1 = int(input('Enter the number from 1 to 12: '))

for i in range(1, 11):
    print(num1, '*', i,  '=', num1 * i)

