'''
Предложите пользователю ввести имя, а затем сообщите, сколько в нем гласных букв.
'''

name = input('Enter your name: ')
l = []
l2 = ['e', 'y', 'u', 'i', 'o', 'a']
for i in name:
    if i in l2:
        l.append(i)
print(len(l))

