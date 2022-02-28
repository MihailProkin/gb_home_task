"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = int(input('Преобразуйте секунды в дни, часы и минуты ! Введите любое число: '))

# Переводим число
# В дни
day_duration = duration // 86400
sec_duration = duration % (24 * 3600)
# В часы
hour_duration = sec_duration // 3600
sec_duration %= 3600
# В минуты
min_duration = sec_duration // 60
sec_duration %= 60

# вывод информации до минуты:
if duration < 60:
    print(f'{duration} сек')
# вывод информации до часа:
elif (duration >= 60) and (duration < 3600):
    print(f'{min_duration} мин {sec_duration} сек')
# вывод информации до суток:
elif (duration >= 3600) and (duration < 86400):
    print(f'{hour_duration} час {min_duration} мин {sec_duration} сек')
else:
    print(f'{day_duration} дн {hour_duration} час {min_duration} мин {sec_duration} сек')
