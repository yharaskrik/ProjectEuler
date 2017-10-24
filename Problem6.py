import math

sum_square = 0
square_sum = 0

for i in range(0, 101):
    sum_square += math.pow(i, 2)
    square_sum += i

print(math.pow(square_sum, 2) - sum_square)