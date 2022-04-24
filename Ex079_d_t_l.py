'''
Создайте пустой список с именем nums. Предложите пользователю последовательно вводить числа. 
После ввода каждого числа добавьте его в конец списка nums и выведите список. 
После того как пользователь введет три числа, спросите, хочет ли он оставить последнее введенное число в списке. 
Если пользователь ответит «no», удалите последний элемент из списка. Выведите список.
'''

nums = []
num1 = int(input('Enter the 1st number: '))
nums.append(num1)
print(nums)
num2 = int(input('Enter the 2nd number: '))
nums.append(num2)
print(nums)
num3 = int(input('Enter the 3rd number: '))
nums.append(num3)
print(nums)
print('Do you wanna save', num3, 'in list?')
answer = input('y or n: ')
if answer == 'n':
    nums.pop()
print(nums)

