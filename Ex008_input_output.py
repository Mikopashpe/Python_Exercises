'''
Предложите пользователю ввести общую сумму счета, а затем запросите общее количество участников обеда. Разделите сумму счета на количество участников и выведите сумму, которую должен заплатить каждый участник.
'''

check = float(input('How much is your check? '))
people = int(input('How many people were there? '))
personal_check = check/people
print('Each guest has to pay', personal_check, '£')

