def odd_num(num):
    for x in range(1, num + 1, 2):
        yield x


if __name__ == "__main__":
    num_gen = odd_num(15)

    print(type(num_gen), list(num_gen))
