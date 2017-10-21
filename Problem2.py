from functools import reduce
import math
import time
millis = time.time()
print(millis)
print(sum(((lambda n: reduce(lambda y, _: y+[y[-1] + y[-2]] if (y[-1] + y[-2] % 2 == 0 and y[-1] + y[-2] < n) else y+[0], range(math.ceil(math.log10(n * math.sqrt(5)) / math.log10((1 + math.sqrt(5)) / 2)) - 2), [0, 1]))(4000000))))
end = time.time()
print(end)
print(end - millis)