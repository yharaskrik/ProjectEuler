from functools import reduce
print(list(filter(lambda x: x % 2 == 0, ((lambda n: reduce(lambda y, _: y+[y[-1] + y[-2]], range(n - 2), [0, 1]))(10)))))