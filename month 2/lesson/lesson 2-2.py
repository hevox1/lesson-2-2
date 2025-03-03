# наследование, полиморфизм, инкапсуляция

'''SUPER CLASS'''
class Robot:
    brain = True
    def __init__(self, name, model, color, destination):
        self.name = name
        self. model = model
        self.color = color
        self.destination = destination


    def __str__(self):
        return f'name is {self.name}\n' \
               f'color is {self.color}\n' \
               f'destination is {self.model}'

    def desti(self):
        print(self.destination)

robot = Robot('litvin', 'youtube', 'blue', 'video')
print(robot)
print(robot.desti())


'''CHILD CLASS'''
class Robot2(Robot):
    brain = False
    def __init__(self, name, model, color, destinations, fly):
        super().__init__(name, model, color, destinations) # наследование
        Robot.__init__(self, name, model, color, destinations) # наследование v2
        self.fly = fly
    def desti(self):
        self.fly = False
        print(self.fly)

robot2 = Robot2('terminator', 't1001', 'pink', 'отбирает одежду', True)
print(robot2.fly)
robot2.desti()

robot.desti()
robot2.desti()
print(robot2.brain, robot.brain)


class Robot3(Robot2):
    def desti(self):
        print(f'{self} теперь он летает')

MegaTron  = Robot3('transformer', 'desipticon', 'red', 'wars', True)
MegaTron.desti()

# class in lesson 2-1
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

Robot3.desti(hum.name)



