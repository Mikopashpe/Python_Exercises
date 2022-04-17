'''
Напишите программу, которая предлагает ввести промежуток времени в днях, а потом выводит количество часов, минут и секунд в этом промежутке.
'''

days = int(input('Enter number of days: '))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print('In', days, 'days:\n', hours, 'hours\n', minutes, 'minutes\n', seconds, 'seconds')

