'''
После получения имени, возраста и размера обуви для четырех человек запросите 
у пользователя имя человека для удаления из списка. 
Удалите эту строку и выведите остальные данные с разбивкой по строкам.
'''

dict_hum = {}

for i in range(4):
    name = input('Enter the name: ')
    age = int(input('Enter the age: '))
    shoes = float(input('Enter the shoes size: '))
    dict_hum[name] = {'Age' : age, 'Shoes size' : shoes}


answer = input("Enter the name: ")
dict_hum.pop(answer)

for key, value in dict_hum.items():
    print(key, value)
    
