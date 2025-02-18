# def human(head, body, foot):
#     print(head, body, foot,)

class Human:
    # атрибуты уровня класса
    head = 1
    body = 1
    hands = 2
    # метод: конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # метод
    def run(self):
        print(f'{self.name} is run')
    def __str__(self):
        return f'name is {self.name}\n ' \
               f'age is {self.age}\n ' \
               f'head is {self.head}'


hum = Human('dmitry', 16)
hum.name = 'kira'
hum.foots = 2

hum.run()
# print(hum, hum.foots)




class Raketa:
    toplivo =True
    kabina = 1
    korpus = 'ironMan'
    human = None
    def run(self, human=1):
        print(f'{human} is fly')


Raketa.run(hum.name)