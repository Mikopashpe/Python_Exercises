'''
Измените программу 102, чтобы она выводила имя и возраст для всех людей в списке, 
но не их размер обуви.
'''

dict_hum = {}

for i in range(4):
    name = input('Enter the name: ')
    age = int(input('Enter the age: '))
    shoes = float(input('Enter the shoes size: '))
    dict_hum[name] = {'Age' : age, 'Shoes size' : shoes}

for name in dict_hum:
    print((name), dict_hum[name]['Age'])

    