from sys import getsizeof

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Ольга',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Анна'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def zip_gen():
    len_klasses = len(klasses)
    return ((x, klasses[i]) if i < len_klasses else (x, None) for i, x in enumerate(tutors))


if __name__ == '__main__':
    a_gen = zip_gen()
    print(type(a_gen))
    print(getsizeof(a_gen))
    print(*a_gen)
