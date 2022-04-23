'''
Создайте список с названиями шести школьных предметов.
Спросите у пользователя, какие из этих предметов ему не нравятся. 
Удалите выбранные предметы из списка и выведите его повторно.
'''

lessons = ['math', 'literature', 'geometry', 'music', 'chemistry', 'history']
while True:
    user_choise = input('Choose what you do not like: ')
    user_choise.lower()
    lessons.remove(user_choise)
    print(lessons)

    