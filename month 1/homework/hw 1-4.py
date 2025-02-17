data_tuple = 'h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g'

letters = []
numbers = []

for element in data_tuple:
    element_type = type(element)
    # print(element_type)
    if element_type == str:
        letters += element
    else:
        numbers.append(element)

# print(letters)
# print(numbers)

numbers.remove(6.13)
numbers.remove(True)
letters.append(True)
numbers.insert(1, 2)
# print(numbers)
# print(letters)

numbers.sort()
# print(numbers)

letters.remove(True)
letters += ('tw')
letters.sort(reverse=True)
# print(letters)

# Преобразование списков в кортеж
number = tuple(numbers)
letter = tuple(letters)

print(data_tuple)
print(letter)
print(number)