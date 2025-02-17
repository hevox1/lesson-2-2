ten = list(range(1, 10+1))
print(ten)
evens = []

for i in ten:
    if i % 2:
        a = 0
    else:
        evens.append(i)
print(evens)

two_list = list(map(lambda x: x**2, evens))
print(two_list)

def index(evens):
    while True:
        for i in evens:
            print('\nexit: 111')
            try:
                ind = int(input('enter your index: '))
                if ind == 111:
                    break
                element = two_list[ind]
                print('element:', element)
            except:
                print('you enter incorrect index!!!')
            continue
        break

index(evens)