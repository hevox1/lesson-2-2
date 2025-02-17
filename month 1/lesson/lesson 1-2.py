#
#
# user_password = input('enter your password: ')
#
# if user_password == password:
#     print('ok')
# else:
#     print('error')
#
# print(len(password))
from operator import ifloordiv

# password = '11'
#
# if len(password) >= 6 and password.isdigit() and not password.isalpha():
#     print('ok')
# else:
#     print(f'твой пароль сост из {len(password)}\n'
#           f'пароль должен состоять из числ и букв, а также длинее 5')

# [start:stop:step]
# word = 'fkjs'

# cut = word[4:]
# print(cut)

# print(word[::3])
# print(word[1:6])
# print(word[0])
# print(word[-3])



shoes_black = '34-38'

first = int(shoes_black[:2])
second = int(shoes_black[3:])

print((second-first) // 2 + 1)






