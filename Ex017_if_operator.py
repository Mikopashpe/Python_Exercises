'''
Предложите пользователю ввести его возраст. 
Если введенное значение равно 18 и более, выведите сообщение «You can vote»; 
если 17 — сообщение «You can learn to drive»; 
если 16 — сообщение «You can buy a lottery ticket». 
Если значение меньше 16, выведите сообщение «You can go Trick- or-Treating».
'''

age = int(input('How old are you? '))


if age >= 18:
    print('You can vote')
elif age == 17:
    print('You can learn to drive')
elif age == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go Trick- or-Treating')

