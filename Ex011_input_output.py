'''
Предложите пользователю ввести число больше 100, а затем число меньше 10. Сообщите, сколько раз меньшее число помещается в большем, в удобном формате.
'''
under100 = int(input('Enter the number under 100: '))
less10 = int(input('Enter the number less then 10: '))
num1 = under100 / less10
print('The first number is', num1, 'times lager')

