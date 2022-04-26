'''
Используя программу из задачи 100, запросите у пользователя имя и регион. 
Выведите соответствующие данные. Запросите у пользователя имя и регион того значения, 
которое он хочет изменить, и позвольте скорректировать объем продаж. 
Выведите объемы продаж по всем регионам для имени, выбранного пользователем.
'''

dict_matrix = {
    'Johnn' : {'N' : 3056, 'S' : 8463, 'E' : 8441, 'W' : 2694}, 
    'Tom' : {'N' : 4832, 'S' : 6786, 'E' : 4737, 'W' : 3612}, 
    'Anna' : {'N' : 5239, 'S' : 4802, 'E' : 5829, 'W' : 1859}, 
    'Fiona' : {'N' : 3904, 'S' : 3645, 'E' : 8821, 'W' : 2451}
}
    
user_name = input('Enter the name from dict: ')
user_region = input('N or S or E or W region? ')
print(dict_matrix[user_name][user_region])

corr_name = input('Enter the name from dict: ')
corr_region = input('N or S or E or W region? ')
answer = int(input('Enter the new value for this region: '))
dict_matrix[corr_name][corr_region] = answer
print(dict_matrix[corr_name])

