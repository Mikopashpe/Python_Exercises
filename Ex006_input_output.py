'''
Спросите, сколько кусков пиццы было у пользователя и сколько кусков он съел. Вычислите, сколько кусков пиццы у него осталось, и выведите результат.
'''

num1 = int(input('How many slices of pizza did you have? '))
num2 = int(input('How many slices of pizza did you eat? '))
num3 = num1 - num2
print('You have', num3, 'slices of pizza')
