'''
Предложите пользователю ввести два числа. Если первое число больше второго, сначала выведите второе число, 
а потом первое. В противном случае выведите сначала первое число, а потом второе.
'''

num1 = int(input('Enter thr first number: '))
num2 = int(input('Enter the second number: '))

if num1 > num2:
    print(num2, num1, sep = ', ')
else:
    print(num1, num2, sep = ', ')

