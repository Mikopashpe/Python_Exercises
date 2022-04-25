'''
Предложите пользователю вводить целые числа. 
Если пользователь вводит число от 10 до 20, сохраните его в массиве; 
в противном случае выведите сообщение «Outside the range». 
После того как пять чисел будут успешно добавлены в массив, выведите сообщение «Thank you» 
и выведите массив, каждый элемент которого находился бы на отдельной строке.
'''
from array import *

new_list = array('i', [])

while len(new_list) < 5:
    num = int(input('Enter num: '))
    if 10<= num <= 20:
        new_list.append(num)
    else:
        print('Outside the range')
print('Thank you')
for i in new_list:
    print(i)