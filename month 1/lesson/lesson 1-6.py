# функции, аргументы *args, **kwargs
# DRY - don`t repeat yourself

# def наименование(параметры):
#     тело функции
#     возврат значения
# наименование(аргументы)

# def len1(sequence: str or list) -> int:
#     '''принимает последовательность, возвращает колв-во элементов в указаной последовательности'''
#     counter = 0
#     for _ in sequence:
#         counter += 1
#     return counter
#
# print(len1('bfudh'))
# print(len1.__doc__)

# w = ' fjhjd'
# l = 0
# for i in w:
#     l += 1
# print(l)


# def greet(name='name', surname='surname'): # обязательный позиционный параметр
#     print(f'name, {name.title()}, surname: {surname.title()}')
#
# greet('azamat', 'fhjdj') # обязательный позиционный аргумент
# '''параметр указывается при создании функции, а аргумент при вызове функции'''
# greet('samat', 'all')
# greet(surname='hdfgskj', name='fgjhd') # keywords arguments (именованные аргументы)
# greet()

# def get_square(width, lenght):
#     return width * lenght
#
# square_2 = get_square(5, 7)
# square_hall = get_square(8, 15)
# print(square_hall)


# width = 5
# lenght = 7
#
# square_2 = width * lenght
# print(square_2)
#
# width = 8
# lenght = 15
# square_hall = width * lenght
# print(square_hall)



# def plus(a, b=0, *args):
#     print(f'a: {a}, b: {b}, args: {args}')
#     return sum(args) / a
#
# print(plus(2, 4, 4, 55,5))


# def days(**kwargs):
#     return sum(kwargs.values())
#
# print(days(monday=1, tuy=2))