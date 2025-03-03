# инкапсуляция
# git clone
from timeit import default_repeat


class Emirlan:
    head = 1
    hands = 2
    foots = 2
    def __init__(self, name='Emirlan', age=18):
        self.__name = name
        self._age = age
    def __str__(self):
        return f'{self.__name}' \
                f'{self._age}'

    def run(self):
        self._run()
        self.__g()
        print(self._age - 1)
        print(self.__name)

    def _run(self):
        print(self.__name, 'run')

    def __g(self):
        pass


# e.name = 'Амир'
# print(e)
# print(e.name)

e = Emirlan()
e.run()
e._run()
print(e._age)
e._age=11
print(e._age)
print(e._Emirlan__name)
e._Emirlan__name='name'
r='fdhesfl'
print(dir(e))






