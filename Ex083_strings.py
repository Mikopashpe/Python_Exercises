'''
Предложите пользователю ввести слово в верхнем регистре. 
Если не все буквы слова будут указаны в верхнем регистре, попросите ввести слово заново. 
Повторяйте попытки, пока пользователь не введет сообщение в верхнем регистре.
'''

word = input('Enter the word in uppercase: ')
again = False
while again == False:
    if word.isupper():
        print('Thank you')
        again = True
    else:
        print('Try again')
        word = input('Enter a message in uppercase: ')
       


