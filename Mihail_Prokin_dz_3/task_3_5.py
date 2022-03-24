"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
   списков (по одному из каждого):
   nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
   adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
   adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

   Например:
   # >>> get_jokes(2)
   ["лес завтра зеленый", "город вчера веселый"]

   Документировать код функции.
   Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
   (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def info(from_, used_, unique):
    while True:
        x_nouns = choice(from_)

        if not (unique and x_nouns in used_):
            used_.append(x_nouns)
            break

    return x_nouns, used_


def get_jokes(count, unique=False):
    """ возвращающую n шуток, сформированных из трех случайных слов """
    used = []
    answer = []

    for _ in range(count):
        nons, used_ = info(nouns, used, unique)
        used.append(used_)

        adv, used_ = info(adverbs, used, unique)
        used.append(used_)

        adj, used_ = info(adjectives, used, unique)
        used.append(used_)

        answer.append(f"{nons} {adv} {adj}")

    return answer


print(get_jokes(2))
