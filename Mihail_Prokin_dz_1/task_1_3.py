"""
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""

for i in range(100):
    str_declension = str(i + 1)
    list_declension = list(str_declension)
    if int(list_declension[-1]) == 1 and i + 1 != 11:
        print(f'{i + 1} процент')
    elif (int(list_declension[-1]) > 1) and (int(list_declension[-1]) <= 4):
        if (i + 1 > 10) and (i + 1 <= 14):
            print(f'{i + 1} процентов')
        else:
            print(f'{i + 1} процентa')
    else:
        print(f'{i + 1} процентов')
