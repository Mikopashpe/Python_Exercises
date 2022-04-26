'''
Предложите пользователю ввести имя, возраст и размер обуви для четырех человек. 
Запросите имя одного из них в списке и выведите значения его возраста и размера обуви.
'''

dict_hum = {}

for i in range(4):
    name = input('Enter the name: ')
    age = int(input('Enter the age: '))
    shoes = float(input('Enter the shoes size: '))
    dict_hum[name] = {'Age' : age, 'Shoes size' : shoes}

print(dict_hum)

answer = input('Enter the name: ')
print(dict_hum[answer])

