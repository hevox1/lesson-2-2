# словари, множества
# {key: value}


student = {
    'name': 'marlen',
    'age': 20,
    'weight': 70.6,
    'born_place': ('bishkek'),
    'hobby': ["chess", 'it']
}
# print(student['hobby'][1])

other_student = dict(name='dima', age=23)

"""add"""
student['favotite_food'] = ['rise', 'fish']

"""edit"""
student['weight'] += 3
student['hobby'] = tuple(student['hobby'])
# print(student)

"""delete"""
delete = student.pop('born_place')
# print(delete)
# del student['hobby'][1]


student.update(other_student)
# print(student.keys())
# print(student.values())
# print(student.items())


"""print"""
# for key, value in student.items():
#     print(key, '==>', value)

# for i in student:
#     print(f'{i}: {student[i]}')



nimbers = {n: n**2 for n in range(1,4)}
# print(nimbers)






numbers = [1, 2, 3, 2, 3, 4, 'a', 'a']
numbers1 = {1, 2, 3, 2, 3, 4, 'a', 'a'}

# print(numbers)


ramen = {'noodles', 'egg', 'pepper'}
beshbarmak = {'noodles', 'onion', 'meat'}
# print(ramen.difference(beshbarmak))
# print(ramen - beshbarmak)
#
# print(ramen.union(beshbarmak))
# print(ramen | beshbarmak)

# print(ramen.intersection(beshbarmak))
# print(ramen & beshbarmak)

# print(ramen.symmetric_difference(beshbarmak))
# print(ramen ^ beshbarmak)

ramen.remove('egg')
ramen.add('water')



menu = {
    'ramen' : {'noodles', 'egg', 'pepper'},
    'beshbarmak' : {'noodles', 'onion', 'meat'}
}

while True:
    user_input = input('print: ')
    if user_input in menu.keys():
        print(menu[user_input])



    # user_input = input('введите продукт: ')
    # for name, ingrs in menu.items():
    #     if user_input in ingrs:
    #         print(name)










