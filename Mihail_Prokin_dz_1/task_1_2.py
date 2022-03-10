"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
   Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
   Внимание: использовать только арифметические операции!
b. * К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
   делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
"""

# Решение задачи b со *

list_cubes_sum = []
count = 0
result = 0

# Создаем список кубов нечетных чисел от 1 до 1000
list_cubes = [(x ** 3) + 17 for x in range(1, 1001) if x % 2 != 0]
#print(list_cubes)
# for x in range(1, 1001, 2):
    # if x % 2 != 0:
        # cubes = (x ** 3) + 17
        # list_cubes.append(cubes)

# Итерация по списку
for i in range(len(list_cubes)):
    # print(list_cubes[i])
    my_str = str(list_cubes[i])
    my_list = list(my_str)
    for a in range(len(my_list)):
        my_list[a] = int(my_list[a])
        # print(my_list)

    # Вычисляем сумму чисел
    for b in range(len(my_list)):
        count += my_list[b]
        # print(count)
    if count % 7 == 0:
        list_cubes_sum.append(count)

# Складываем все числа в списке
for c in list_cubes_sum:
    result += c

print(result)
# print(sum(list_cubes_sum))
