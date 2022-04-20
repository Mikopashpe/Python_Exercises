'''
Создайте переменную с именем compnum и присвойте ей значение 50. 
Предложите пользователю ввести число. Пока предположение не совпадает со значением compnum, 
сообщите, больше оно или меньше compnum, и предложите ввести другое число. 
Если введенное значение совпадет с compnum, выведите сообщение «Well done, you took [попытки] attempts».
'''

compnum = 50
answer = 'y'
num = int(input('Enter the number: '))
attempts = 1


while num != compnum:
    if num < compnum:
        print('Low')
    else:
        print('High')
    attempts += 1
    num = int(input('Another number: '))
print('Well done, you took', attempts, 'attempts')


