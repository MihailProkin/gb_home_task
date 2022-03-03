"""
2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
   с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
   # >>> num_translate_adv("One")
   "Один"
   # >>> num_translate_adv("two")
   "два"
"""

dict_str_num = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
}


def num_translate_adv(str_num):
    """ конвертировать zero в ноль ... nine в девять и начинающимися с заглавной буквы """
    key = dict_str_num.get(str_num.lower())

    if key:
        return key.capitalize() if str_num[0].isupper() else key


print(num_translate_adv('Zero'))
