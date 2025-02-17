# списки \ кортежи
# list - список
# tuple - кортеж

new = list('oop')
new1 = list(range(1, 4))
print(new, new1)
# ['o', 'o', 'p'] [1, 2, 3]

objects = ['python', 'geek', 5, 8, True, False, 4.7, 20.5, new]
print(objects)

# меняем местами
objects[0], objects[3] = objects[3], objects[0]


# добавление обьекта в конец списка:
# objects.append('rostov')
# print(objects)

# если мы хотим что нибудь добавить в определенное место в списке:
# objects.insert(3, 'water')
# print(objects)

# добавляем список в кортеж
# objects.append(new)
# print(objects)
# ['python', 'geek', 5, 'water', 8, True, False, 4.7, 'rostov', ['o', 'o', 'p']]

objects.extend(new) # or objects += new
print(objects)
# ['python', 'geek', 5, 'water', 8, True, False, 4.7, 'rostov', 'o', 'o', 'p']



# DELETE

objects.remove(True)
objects.remove(4.7)
print(objects)
# ['python', 'geek', 5, 'water', 8, False, 'rostov', 'o', 'o', 'p']

# delete of index
objects.pop(1)
print(objects)
# ['python', 5, 'water', 8, False, 'rostov', 'o', 'o', 'p']

deleted = objects.pop(1)
print(deleted)
# 5

del objects[-2]
del objects[4:7]
print(objects)
# ['python', 'water', 8, False]

# списковое включение, удаление всех строк
objects = [i for i in objects if type(i) != str]

# objects[0] = objects[0].title()

# objects[3] += 15

# del objects[-1][1:], objects[-1][1]

# objects[0], objects[3] = objects[3], objects[0]

# objects.sort() # or сортировка в обратную сторону # objects.sort(reverse=True)

# print(min(objects))
# print(max(objects))