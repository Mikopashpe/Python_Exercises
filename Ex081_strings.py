'''
Предложите пользователю ввести его любимый школьный предмет. 
Выведите его так, чтобы после каждой буквы следовал дефис — например, S-p-a-n-i-s-h-.
'''

lesson = input('Your favorite lesson at school? ')
for i in lesson:
    print(i, end = '-')

    