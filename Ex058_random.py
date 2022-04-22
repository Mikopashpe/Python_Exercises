'''
 Напишите математическую игру, в которой пользователь должен ответить на пять вопросов. 
 Каждый вопрос строится из двух случайно сгенерированных целых чисел (например, [num1] + [num2]). 
 Предложите пользователю ввести ответ. 
 Если пользователь ввел правильный ответ, добавьте одно очко в его пользу. 
 В конце игры сообщите пользователю количество правильных ответов.
 '''

 
import random

counter = 0
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
a1 = num1 + num2
print(num1, '+', num2)
answer1 = int(input('Resultl: '))
if answer1 == a1:
     counter += 1
     print(counter)
num3 = random.randint(1, 10)
num4 = random.randint(1, 10)
a2 = num3 - num4
print(num3, '-', num4)
answer2 = int(input('Result: '))
if answer2 == a2:
    counter += 1
    print(counter)
num5 = random.randint(1, 10)
num6 = random.randint(1, 10)
a3 = num5 * num6
print(num5, '*', num6)
answer3 = int(input('Result: '))
if answer3 == a3:
    counter += 1
    print(counter)
num7 = random.randint(1, 10)
a4 = num7 ** 2
print(num7, '**2')
answer4 = int(input('Result: '))
if answer4 == a4:
    counter += 1
    print(counter)
num8 = random.randint(1, 10)
num9 = random.randint(1, 10)
a5 = (num8 + num9) * 2
print('(', num8, '+', num9, ') * 2')
answer5 = int(input('Result: ')) 
if answer5 == a5:
    counter += 1
print('Right answers:', counter)


