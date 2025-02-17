# работа с файлами
# w - write
# a - add
# r - read
# x - safety mod


# new = open('file.txt', 'w', encoding='UTF-8')
# new.write('Россия, ростов')
# new.close()


'''mod w'''
# with open('new.txt', 'w', encoding='UTF-8') as file:
#     file.write('something123')

'''mod a'''
# with open('new.txt', 'a', encoding='UTF-8') as file:
#     file.write('\n222222')

'''mod x'''
# with open('text.txt', 'x', encoding='UTF-8') as file:
#     file.write('dhdks')

# from time import sleep
# '''mod r'''
# with open('new.txt', 'r', encoding='UTF-8') as file:
#     # print(file.read())
#     for letter in file.readlines():
#         sleep(1)
#         print(letter, end='')
#     print(file.readlines()[0].split()[0])


# while True:
#     filename = input('name file: ')
#     if filename == 'exit':
#         break
#     with open(f'{filename}.txt', 'w', encoding='UTF-8') as file:
#         file.write(input('what should we write down? \n'))




'''программа которая задает студенту число и потом записывает все в новый файл.txt'''
# from random import randint, choice
#
# students = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# while len(students) != 0:
#     print(students)
#     first, second = randint(1, 12), randint(12, 99)
#     right = first * second
#     student_id = choice(students)
#     name = input(f'name students {student_id}: ').title()
#     try:
#         user_answer = int(input(f'{name}, сколько будет {first} * {second}?\n'))
#     except:
#         print('only int!!!')
#     if user_answer == right:
#         print("good")
#         with open('test.txt', 'a', encoding='UTF-8') as file:
#             file.write(
#                 f'{name}: {first} * {second} = {user_answer} ({right})'
#                 f' right\n'
#             )
#     else:
#         print(f'incorrect, {right}')
#         with open('test.txt', 'a', encoding='UTF-8') as file:
#             file.write(
#                 f'{name}: {first} * {second} = {user_answer} ({right})'
#                 f' not true\n'
#             )
#     students.remove(student_id)


data =  {}

with open('test.txt', 'r', encoding='UTF-8') as file:
    for i in file.readlines():
        data[i.split()[0]] = i.split()[-1]

print(
    f'кол-во: {len(data)}\n'
    f'right: {list(data.values()).count("not true")}\n'
    f'список имен: {set`    (data.keys())}'
)