# lambda
# lambda arguments: expression

# a = lambda a,  b: a + b
# print(a(2 ,4))
#
# def b(a, b):
#     return a + b
# print(b(3, 2))


# def up_leter(word: str):
#     return word.title()
#
# def show_words(sequance, func):
#     for word in sequance:
#         print(func(word))
#
# show_words(['fh, fjhd, fdj'], up_leter)
# show_words(['fh, fjhd, fdj'], len)


# numbers = list(range(1, 11))
# # print(numbers)
# # # map_list = list(map(lambda x: x * 2, numbers))
# # map_list = [i*3 for i in numbers]
# # print(map_list)
#
# fil_numbers = list(filter(lambda x: x > 6, numbers))
# print(fil_numbers)

#
# def last(word: str) -> str:
#     return word[:-1] + word[-1].upper()

# a = last('python')
# print(a)


# current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
# sorted_list = lambda x: (sorted(i) for i in x)
# print(sorted_list)
# second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
# result = second_largest(current_list, sorted_list)
# print(result)

# new = [sorted(i) for i in current_list]
# print(new)
#
# for i in new:
#     print(i[len(i) - 2])


# print(10/0)
# try:
#     print(10/0)
# except:
#     print('not')

# if ZeroDivisionError:
#     print('not')
# else:
#     print(10/0)


# word = 'autumn'
#
# while True:
#     user = input('season')
#     if user != word:
#         raise  Exception('incorrect season')

    # try:
    #     us = int(input('print index: '))
    #     print(word[us])
    # except IndexError:
    #     print('not legit index')
    # except ValueError:
    #     print('only numbers!')
    # finally:
    #     word = 'geek'
    #     print('end')



