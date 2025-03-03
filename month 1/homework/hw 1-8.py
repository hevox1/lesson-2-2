print('загадайте число от 1 до 100')
left, right = 0
while True:
    user = input()
    mid = left = (right - left) // 2
    if mid == user:
        print('вы загадали число:', mid)



