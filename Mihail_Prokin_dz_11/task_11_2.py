class MyZeroDiv(Exception):
    def __int__(self, *args: object) -> None:
        super.__init__(*args)


if __name__ == '__main__':
    from sys import exit

    a = 0
    b = 0
    try:
        a = float(input('Введите число "a": '))
        b = float(input('Введите число "b": '))
    except:
        print('Вы вводите не число!')
        exit(1)

    try:
        if b == 0:
            raise MyZeroDiv('Делить на ноль нельзя')
        print(f'Все в порядке: {a} / {b} = {a/b}')
    except MyZeroDiv as ex:
        print(ex)
