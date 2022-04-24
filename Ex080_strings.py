'''
Предложите пользователю ввести свое имя, а затем выведите длину имени. 
Запросите фамилию и выведите длину фамилии. Соедините имя с фамилией, разделив их пробелом,
и выведите результат. Наконец, выведите длину полного имени (включая пробел).
'''

fname = input('Enter your first name: ')
print(len(fname))
sname = input('Enter your surname: ')
print(len(sname))
fullname = fname + ' ' + sname
print(fullname)
print(len(fullname))

