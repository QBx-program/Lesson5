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

# Задача 2

odd_to_2 = (num for num in range(1, get_num+1, 2))

for i in range(1, get_num + 1, 2):
    print(next(odd_to_2))

# Задача 3

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

for i in range(len(tutors) - len(klasses)):
    if len(tutors) - len(klasses) > 0:
        klasses.append(None)

tupple_new = ((v_1, v_2) for v_1, v_2 in zip(tutors, klasses))

print(f'Это генератор: {type(tupple_new)}')
print(*tupple_new)