'''
Спросите у пользователя, в каком направлении он хочет вести отсчет (в прямом или обратном). 
Если выбран прямой отсчет, запросите число и проведите отсчет от 1 до введенного числа. 
Если выбран обратный отсчет, запросите число меньше 20, а затем проведите обратный отсчет 
от 20 до заданного числа. Если введено что-то другое, выведите сообщение «I don't understand».
'''

answer = input('Choose a reference direction (< or >): ')


if answer == '>':
    num = int(input('Enter the number: '))
    for i in range(1, num + 1):
        print(i)
elif answer == '<':
    num = int(input('Enter the number less than 20: '))
    for i in range(20, num - 1,  -1):
        print(i)
else:
    print('I don\'t understand')

    