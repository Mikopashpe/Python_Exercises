'''
Создайте список из четырех трехзначных чисел. 
Выведите содержимое списка, при этом каждый элемент должен выводиться на отдельной строке. 
Предложите пользователю ввести число из трех цифр. 
Если введенное число совпадает с одним из чисел в списке, выведите позицию этого числа;
в противном случае выведите сообщение «That is not in the list».
'''

l1 = [111, 222, 333, 444]

for i in l1:
    print(i)
user = int(input('Enter the number: '))
if user in l1:
    print(l1.index(user))
else:
    print('That is not in the list')

