'''
Предложите пользователю ввести сначала имя, а затем фамилию. 
Соедините их, разделив пробелом, после чего выведите полное имя и его длину.
'''

firstname = input('Enter your firstname: ')
surname = input('Enter your surname: ')
fullname = firstname + ' ' + surname

print(fullname, len(fullname), sep = ', ')