from functools import reduce
import math
import time
total_millis = 0
counter = 0
for k in range(0, 100000):
    millis = time.time()
    sum(list(filter(lambda x: (x % 2 == 0 and x < 4000000), ((lambda n: reduce(lambda y, _: y+[y[-1] + y[-2]], range(int(math.ceil(math.log10(n * math.sqrt(5)) / math.log10((1 + math.sqrt(5)) / 2))) - 2), [0, 1]))(4000000)))))
    total_millis += (time.time() - millis)
    counter += 1
print(total_millis / counter)