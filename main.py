# Задача 1

def odd_nums(num):
    for i in range(1, num+1, 2):
        yield i

while True:
    get_num = input('Введите число ')
    if get_num.isdigit():
        get_num = int(get_num)
        break

odd_to = odd_nums(get_num)

for i in range(1, get_num+1, 2):
    print(next(odd_to))