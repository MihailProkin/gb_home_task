import os
import sys

size = {}


def scan_mem(pth):
    for root, _, files in os.walk(pth):
        for file in files:
            correct_file = os.path.join(root, file)
            mem = 10 ** len(str(os.stat(correct_file).st_size))
            size[mem] = size.get(mem, 0) + 1


if __name__ == '__main__':

    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()
    scan_mem(pth)
    print(size)
