""""
5. Создать список, содержащий цены на товары (10–20 товаров), например:
   [57.8, 46.51, 97, ...]

a. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
   (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
   получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
b. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки
   остался тот же).
c. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
d. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

prices = [57.8, 46.51, 37, 97.5, 66.89, 35.8, 77.22, 20, 45.88, 99.9, 44, 21.3, 54.68]
print(prices, id(prices))

end_word: str = ", "

print(f"{'a':-^95}")

for x in prices:
    if isinstance(x, int):
        a = float(x)
        x = str(x).split('.')
        a = x[0]
        b = str(0) + '0'
    elif isinstance(x, float):
        x = str(x).split('.')
        a = int(x[0])
        b = int(len(x[1]))
        if b == 1:
            b = '0' + x[1]
        elif b == 2:
            b = x[1]
    elif x == len(prices) - 1:
        end_word = "\n"
    print(f"{a} руб {b} коп", end=end_word)

print(f"{'>>>':-^1}")

print(f"{'b':-^95}")

prices.sort()
print(prices, id(prices))

print(f"{'c':-^95}")

copy_prices = prices.copy()
copy_prices = sorted(copy_prices, reverse=True)
print(copy_prices, id(copy_prices))

print(f"{'d':-^95}")

most_expensive_goods = copy_prices[0:5]
most_expensive_goods.sort()
print(most_expensive_goods)
