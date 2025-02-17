# for

# cash = 100
# percents = 0.1
# years = 5
#
# counter = 1
#
# for years in range(1, years + 1):
#     cash = round(cash * percents + cash, 1)
#     print(f'year: {counter} - {cash}')
#     counter += 1


# word = 'аксессуар'
#
# for letter in word:
#     if letter == 'у':
#         print('мы пропускакем у')
#         continue
#     print(letter)

    # if letter == 'е':
    #     break
    # print(letter)

    # print(letter.upper(), end='')

# for i in range(1, 4):
#     for k in range(1, 4):
#         print(i, k)



# while

# c = 0
#
# while c != 101:
#     c += 1
#     print('d')
#     if c == 100:
#         break


eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,. "
rus = "йцукенгшщзхъфывапролджэячсмитьбю "

while True:
    user = input('\nenter word: ').lower()

    for i in user:
        if i in eng:
            print(rus[eng.index(i)], end = '')
        else:
            print(eng[rus.index(i)])
    # else:
    #     print('error')

