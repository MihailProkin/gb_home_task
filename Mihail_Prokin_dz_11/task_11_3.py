class NoAllNumb(Exception):

    def __int__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == '__main__':

    lst = []
    while True:
        try:
            inp = input()
            if inp == 'stop':
                break
            elif not inp.isdigit():
                raise NoAllNumb()
            else:
                lst.append(int(inp))
        except NoAllNumb:
            print('Вы вводите не число')

    print(*lst)

