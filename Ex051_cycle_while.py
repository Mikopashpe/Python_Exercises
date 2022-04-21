'''
Выведите строки «There are [счетчик] green bottles hanging on the wall, 
[счетчик] green bottles hanging on the wall, and if 1 green bottle should accidentally fall». 
Затем выведите вопрос: «how many green bottles will be hanging on the wall?». 
Если пользователь ответит правильно, выведите сообщение «There will be [счетчик] green bottles hanging on the wall». 
Если пользователь ответит неправильно, выведите сообщение «No, try again», пока не будет дан правильный ответ. 
Когда счетчик уменьшится до 0, выведите сообщение «There are no more green bottles hanging on the wall».
'''

counter = 10
num = 0

while counter != 0:
    print('There are', counter, 'green bottles hanging on the wall,', counter, 'green bottles hanging on the wall,\nand if 1 green bottle should accidentally fall')
    num = int(input('how many green bottles will be hanging on the wall? '))
    if num != counter:
        print('No, try agai')
    else:
        print('There will be', counter, 'green bottles hanging on the wall')
    counter -= 1
print('There are no more green bottles hanging on the wall') 

