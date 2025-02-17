# Козерог: 23 декабря — 20 января.
# Водолей: 21 января — 19 февраля.
# Рыбы: 20 февраля — 20 марта.
# Овен: 21 марта — 20 апреля.
# Телец: 21 апреля — 21 мая.
# Близнецы: 22 мая — 21 июня.
# Рак: 22 июня — 22 июля.
# Лев: 23 июля — 21 августа.
# Дева: 22 августа — 23 сентября.
# Весы: 24 сентября — 23 октября.
# Скорпион: 24 октября — 22 ноября.
# Стрелец: 23 ноября — 22 декабря.

# we receive data from the user
day = int(input('enter your birthday: '))
month = int(input('enter your month of birth: '))

# processing data for screen
if ((day >= 23 < 32) and month == 12) or ((day >= 1 < 21) and month == 1):
    print('козерог')
elif ((day >= 21 < 32) and month == 1) or ((day >= 1 < 20) and month == 2):
    print('водолей')
elif ((day >= 20 < 32) and month == 2) or ((day >= 1 < 21) and month == 3):
    print('рыбы')
elif ((day >= 21 < 32) and month == 3) or ((day >= 1 < 21) and month == 4):
    print('овен')
elif ((day >= 21 < 32) and month == 4) or ((day >= 1 < 22) and month == 5):
    print('телец')
elif ((day >= 22 < 32) and month == 5) or ((day >= 1 < 22) and month == 6):
    print('близнецы')
elif ((day >= 22 < 32) and month == 6) or ((day >= 1 < 23) and month == 7):
    print('рак')
elif ((day >= 23 < 32) and month == 7) or ((day >= 1 < 22) and month == 8):
    print('лев')
elif ((day >= 22 < 32) and month == 8) or ((day >= 1 < 24) and month == 9):
    print('дева')
elif ((day >= 24 < 32) and month == 9) or ((day >= 1 < 24) and month == 10):
    print('весы')
elif ((day >= 24 < 32) and month == 10) or ((day >= 1 < 23) and month == 11):
    print('скорпион')
elif ((day >= 23 < 32) and month == 11) or ((day >= 1 < 23) and month == 12):
    print('стрелец')
else:
    print('incorrect data entered')


