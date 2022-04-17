'''
Предложите пользователю ввести первую строку какого- нибудь стихотворения, 
выведите длину строки. 
Запросите начальную и конечную позицию и выведите только эту часть строки 
(не забудьте, что в Python нумерация индексов начинается с 0, а не с 1).
'''

text = input('Enter the phrase: ')
print('Lenght is', len(text))
start = int(input('Enter start: '))
end = int(input('Enter end: '))
part = (text[start:end])
print(part)

