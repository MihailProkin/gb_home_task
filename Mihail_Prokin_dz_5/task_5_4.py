import sys
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

my_result = []
start = perf_counter()

for i, j in zip(src, src[1:]):
    if j > i:
        my_result.append(j)

print(perf_counter() - start, sys.getsizeof(my_result), my_result)

start = perf_counter()
my_result = [j for i, j in zip(src, src[1:]) if j > i]
print(perf_counter() - start, sys.getsizeof(my_result), my_result)
