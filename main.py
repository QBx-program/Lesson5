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

gen = [None for i in range(len(tutors) - len(klasses)) if len(tutors) - len(klasses) > 0]
klasses.extend((i for i in gen))
tupple_new = ((v_1, v_2) for v_1, v_2 in zip(tutors, klasses))

print(f'Это генератор: {type(tupple_new)}')
print(*tupple_new)

# Задача 4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([n for i, n in enumerate(src) if n > src[i - 1]])

# Задача 5

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res = [n for n in src if src.count(n) == 1]
print(res)