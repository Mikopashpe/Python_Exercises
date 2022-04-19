'''
Измените программу из упражнения 35 так, чтобы она предлагала пользователю ввести имя и число, 
а затем выводила имя заданное количество раз
'''

username = input('Enter your name: ')
end = int(input('How many times? '))

for i in range(0, end):
    print(username)

    