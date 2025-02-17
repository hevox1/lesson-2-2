# def наименование(параметры):
#     тело функции
#     возврат значения
# наименование(аргументы)


def ar_mean(**kwargs):
    '''функция принимающая неограниченное кол-во чисел и возвращающая их среднее арифметическое'''
    return int(sum(kwargs.values()) / len(kwargs))

print(ar_mean(a=8, b=8, d=4, jf=3))
print(ar_mean.__doc__)


def check(password):

    for i in password:
        '''функция проверяющая длину пароля; наличие минимум одной буквы и числа'''
        if len(password) > 6 and i.isnumeric() and i.isdigit():
            return True
        else:
            return False

print(check('84dhfjds3'))
print(check.__doc__)





